
from django import template

from services.models import Course

register = template.Library()

@register.simple_tag
def has_courses(user):
    return bool(Course.objects.filter(owner=user).exists())