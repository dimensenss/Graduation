from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import EmailValidator

from clients.models import Client
from clients.utils import validate_email


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Client
        fields = ('email', 'first_name', 'last_name', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")

    def clean_email(self):
        email = self.cleaned_data['email']
        validate_email(self, email)
        return email


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = Client
        fields = ('email', 'password')

    def confirm_login_allowed(self, user):
        if not user.is_verified:
            raise forms.ValidationError("Ваш обліковий запис неактивний. Перевірте електронну пошту для підтвердження.", code='inactive', )
