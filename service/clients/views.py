from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView
from rest_framework.authtoken.models import Token


from clients.forms import RegisterUserForm
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
                user.is_active = True
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


class ActivateClientView(View):
    template_name = 'clients/activate_jwt.html'

    def get(self, request, *args, **kwargs):
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        return render(request, self.template_name, context={"uid": uid, "token": token})
