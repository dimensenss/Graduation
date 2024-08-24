from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.forms import forms

from clients.models import Client


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ('email', 'first_name', 'last_name', 'password', )