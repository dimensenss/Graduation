from django.core.validators import MinValueValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from clients.models import Client
from services.models import Course, CourseInfo

# class CourseInfoSerializer(serializers.ModelSerializer):
#     preview_video = serializers.FileField(required=False)
# class Meta:
#         model = CourseInfo
#         fields = ['workload', 'authors', 'preview_video',]

# class CourseUpdateSerializer(serializers.ModelSerializer):
#     workload = serializers.CharField(source='info.workload', required=False)
#     authors = serializers.PrimaryKeyRelatedField(source='info.authors', queryset=Client.objects.all(), many=True,
#                                                  required=False)
#     # authors = serializers.CharField(source='info.authors', required=False)
#     preview_video = serializers.FileField(source='info.preview_video', required=False)
#
#     class Meta:
#         model = Course
#         fields = ['course_name', 'cat', 'description', 'language', 'difficulty', 'preview', 'workload', 'authors',
#                   'preview_video', ]
#
#     def update(self, instance, validated_data):
#         instance.course_name = validated_data.get('course_name', instance.course_name)
#         instance.cat = validated_data.get('cat', instance.cat)
#         instance.description = validated_data.get('description', instance.description)
#         instance.language = validated_data.get('language', instance.language)
#         instance.difficulty = validated_data.get('difficulty', instance.difficulty)
#         instance.preview = validated_data.get('preview', instance.preview)
#
#         info_data = validated_data.pop('info', {})
#
#         # Обрабатываем связанные модели CourseInfo
#
#         if info_data:
#             info = instance.info  # Получаем связанную запись CourseInfo
#             info.workload = info_data.get('workload', info.workload)
#             info.preview_video = info_data.get('preview_video', info.preview_video)
#
#             # Обрабатываем ManyToMany поле authors
#             if 'authors' in info_data:
#                 new_authors = info_data['authors']
#                 existing_authors = set(info.authors.all())
#                 new_authors_set = set(new_authors)
#                 new_authors_ids = [str(author.id) for author in new_authors]
#
#                 # Проверяем, если автор уже в списке
#                 for author in new_authors_set:
#                     if author in existing_authors:
#                         raise serializers.ValidationError(f"Автор с ID {author.id} уже добавлен.")
#                     info.authors.add(author)
#
#             info.save()
#         instance.save()
#         return instance
from rest_framework import serializers


# class CourseUpdateSerializer(serializers.ModelSerializer):
#     preview_video = serializers.FileField(source='info.preview_video', required=False)
#     authors = serializers.CharField(source='info.authors',required=False)
#     workload = serializers.CharField(source='info.workload',required=False)
#
#     class Meta:
#         model = Course
#         fields = ['id', 'course_name', 'description', 'full_price', 'language', 'difficulty', 'have_certificate',
#                   'preview', 'preview_video', 'authors', 'workload']




class CourseUpdateSerializer(serializers.ModelSerializer):
    workload = serializers.IntegerField(source='info.workload', required=False, validators=[MinValueValidator(0)])
    authors = serializers.CharField(source='info.authors', required=False)
    preview_video = serializers.FileField(source='info.preview_video', required=False)

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'description', 'full_price', 'language', 'difficulty', 'have_certificate',
                  'preview', 'workload', 'authors', 'preview_video']


