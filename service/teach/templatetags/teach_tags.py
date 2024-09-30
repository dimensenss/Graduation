
from django import template

from services.models import Course
import re


register = template.Library()

@register.simple_tag
def has_courses(user):
    return bool(Course.objects.filter(owner=user).exists())


def get_youtube_video_id(url):
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None
@register.simple_tag
def get_youtube_thumbnail_url(youtube_url):
    video_id = get_youtube_video_id(youtube_url)
    if video_id:
        return video_id
    return None

