from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView, TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from services.models import CourseModules, Course
from teach.mixins import OwnerPermissionMixin
from teach.permissions import IsOwner
from teach.serializers import CourseModuleSerializer


class TeachCourseModulesView(LoginRequiredMixin, OwnerPermissionMixin, ListView):
    template_name = 'teach/teach_course_modules.html'
    context_object_name = 'modules'

    def get_object(self):
        return Course.objects.prefetch_related('modules').get(pk=self.kwargs['pk'])

    def get_queryset(self):
        return CourseModules.objects.filter(course__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_object()
        return context


class CreateModuleAPI(ModelViewSet):
    permission_classes = (IsOwner,)
    serializer_class = CourseModuleSerializer
    queryset = CourseModules.objects.all()

    def get_object(self):
        module = CourseModules.objects.create(course_id=self.kwargs['pk'])
        return module

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        response = render_to_string(
            'includes/teach_module_form.html', {'module': instance}, request=request
        )
        return JsonResponse(response)
