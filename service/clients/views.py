from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from clients.forms import RegisterUserForm, LoginUserForm
from clients.models import Client
from clients.serializers import ActivationEmailSerializer
from clients.tasks import send_activation_email
from clients.utils import render_activation_email



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None:
        try:
            token_obj = Token.objects.get(user=user)
            if token_obj.key == token:
                user.is_verified = True
                user.save()
                auth.login(request, user)
                messages.success(request, f"Акаунт {user.email} активовано.")
                return redirect('services:index')
        except Token.DoesNotExist:
            pass

    return render(request, 'clients/activation_invalid.html')




class RegisterClientView(CreateView):
    template_name = 'clients/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('services:index')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        to_email = form.cleaned_data.get('email')
        message = render_activation_email(self.request, user.id)
        send_activation_email.delay('Підтвердження реєстрації', message, to_email)

        messages.success(self.request, f"Лист для активації відправлено на {to_email}. Перевірте вашу пошту.")
        return redirect(self.success_url)

    def form_invalid(self, form):
        return HttpResponseBadRequest(form.errors)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реєстрація'
        return context

class UserLoginView(LoginView):
    template_name = 'clients/login.html'
    form_class = LoginUserForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(self.request, f"Ви вже авторизовані")
            return redirect('services:index')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        # redirect_page = self.request.POST.get('next', None)
        # if redirect_page and redirect_page != reverse('clients:logout'):
        #     return redirect_page
        return reverse_lazy('services:index')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()

        if user:
            if not user.is_active:
                messages.error(self.request, "Ваша електронна пошта не підтверджена.")
                return redirect('clients:login')

            auth.login(self.request, user)
            if session_key:
                #
                # forgotten_cart = Cart.objects.filter(user=user)
                # if forgotten_cart.exists():
                #     forgotten_cart.delete()
                #
                # Cart.objects.filter(session_key=session_key).update(user=user)
                messages.success(self.request, f"Ви авторизовані")

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизація'
        return context


@login_required
def logout_user(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Ви вийшли з акаунту')
        return redirect('services:index')

class ActivateClientView(View):
    template_name = 'clients/activate_jwt.html'

    def get(self, request, *args, **kwargs):
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        return render(request, self.template_name, context={"uid": uid, "token": token})


class SendActivationEmailView(APIView):
    def post(self, request):
        serializer = ActivationEmailSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            user = Client.objects.get(email=data['to_email'])
            message = render_activation_email(self.request, user.id)

            send_activation_email.delay(data['subject'], message, data['to_email'])
            messages.success(request, f"Лист для активації відправлено на {data['to_email']}. Перевірте вашу пошту і увійдіть")
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
