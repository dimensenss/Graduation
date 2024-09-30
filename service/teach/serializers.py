from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError
from services.models import Course, CourseModules
from rest_framework import serializers


def validate_preview_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Розмір файла не повинен перевищувати 5MB.')

class CourseUpdateSerializer(serializers.ModelSerializer):
    workload = serializers.IntegerField(source='info.workload', required=False, validators=[MinValueValidator(0)])
    authors = serializers.CharField(source='info.authors', required=False)
    preview_video = serializers.URLField(source='info.preview_video', required=False)
    preview = serializers.ImageField(required=False, validators=[validate_preview_size])  # Добавление кастомного валидатора

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'full_price', 'language', 'difficulty', 'have_certificate',
                  'preview', 'workload', 'authors', 'preview_video']

class CourseModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseModules
        fields = ['title', 'description', 'order']


