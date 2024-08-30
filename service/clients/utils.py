import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.authtoken.models import Token

User = get_user_model()


def generate_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key


def render_activation_email(request, user_id):
    user = User.objects.get(pk=user_id)
    current_site = get_current_site(request)
    message = render_to_string('clients/activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user_id)),
        'token': generate_auth_token(user),
    })
    return message

def validate_email(user, email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) and len(email) > 254:
        raise forms.ValidationError("Некоректний формат email адреси")

    if User.objects.filter(email=email).exists() and user.instance.email != email:
        raise forms.ValidationError("Користувач з такою адресою електронної пошти вже існує")



# def validate_username(email):
#     if SocialAccount.objects.filter(user__email=email).exists():
#         raise forms.ValidationError(
#             "Ця адреса електронної пошти зареєстрована через соціальну мережу. "
#             "Будь ласка, увійдіть через відповідну соціальну мережу.")
