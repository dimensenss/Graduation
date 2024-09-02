from celery import shared_task
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from clients.utils import generate_auth_token, User


@shared_task
def send_activation_email(subject, message, to_email):
    msg = EmailMultiAlternatives(subject=subject,
                                 to=[to_email])
    msg.attach_alternative(message, 'text/html')
    msg.send()