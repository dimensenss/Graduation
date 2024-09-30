from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from services.models import Course, CourseInfo, CourseModules


class CourseCreateForm(forms.ModelForm):
    course_name = forms.CharField(min_length=3, max_length=50)
    captcha = ReCaptchaField(widget= ReCaptchaV2Checkbox(), required=True)
    class Meta:
        model = Course
        fields = ('course_name',)

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'cat', 'description', 'language', 'difficulty', 'preview']

class CourseInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = CourseInfo
        fields = ['workload', 'authors', 'preview_video']


class CourseModuleForm(forms.ModelForm):
    class Meta:
        model = CourseModules
        fields = ['title', 'description', 'order']

