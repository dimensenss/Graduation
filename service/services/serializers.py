from rest_framework import serializers

from services.models import Course, CourseModules, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'video_url')


class SubCategoriesSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModules
        fields = ('id', 'title', 'lessons')


class CourseSerializer(serializers.ModelSerializer):
    subcategories = SubCategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'owner', 'course_name', 'full_price', 'subcategories')
