from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from services.models import Course
from services.serializers import CourseSerializer


class CoursesAPIView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class IndexView(ListView):
    template_name = 'index.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
