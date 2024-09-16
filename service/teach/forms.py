from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from services.models import Course


class CourseCreateForm(forms.ModelForm):
    captcha = ReCaptchaField(widget= ReCaptchaV2Checkbox(), required=True)
    class Meta:
        model = Course
        fields = ('course_name',)