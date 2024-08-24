from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from clients.forms import RegisterUserForm
from clients.models import Client
from clients.serializers import ClientSerializer


class RegisterClientView(CreateView):
    template_name = 'clients/register.html'
    form_class = RegisterUserForm


class ActivateClientView(View):
    template_name = 'clients/activate.html'

    def get(self, request, *args, **kwargs):
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        return render(request, self.template_name, context={"uid": uid, "token": token})
