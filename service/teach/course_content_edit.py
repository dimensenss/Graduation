from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from services.models import CourseModules, Course, Lesson
from teach.mixins import OwnerPermissionMixin
from teach.permissions import IsOwner
from teach.serializers import CourseModuleSerializer, CourseLessonSerializer


class TeachCourseModulesView(LoginRequiredMixin, OwnerPermissionMixin, ListView):
    template_name = 'teach/teach_course_modules.html'
    model = CourseModules
    context_object_name = 'modules'

    def get_course(self):
        return Course.objects.get(pk=self.kwargs['pk'])

    def get_queryset(self):
        return CourseModules.objects.filter(course_id=self.kwargs['pk']).prefetch_related(
            Prefetch('lessons', queryset=Lesson.objects.order_by('id'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context


class CreateModuleAPI(ModelViewSet):
    permission_classes = (IsOwner,)
    serializer_class = CourseModuleSerializer
    queryset = CourseModules.objects.all()

    def get_object(self):
        module = CourseModules.objects.create(course_id=self.kwargs['pk'])
        return module

    def get_course(self):
        return Course.objects.get(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        module_form = render_to_string(
            'includes/teach_module_form.html', {'module': instance}, request=request
        )
        response = {
            'module_form': module_form
        }

        return JsonResponse(response)


class CreateLessonAPI(ModelViewSet):
    permission_classes = (IsOwner,)
    serializer_class = CourseLessonSerializer
    queryset = Lesson.objects.all()

    def create_lesson(self, module_id):
        try:
            return Lesson.objects.create(course_module_id=module_id)
        except Lesson.DoesNotExist:
            return None

    def get_lesson(self, lesson_id):
        try:
            return Lesson.objects.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            return None

    def get_course(self):
        return Course.objects.get(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        module_id = request.data.get('module_id')
        instance = self.create_lesson(module_id)
        lesson_form = render_to_string(
            'includes/teach_lesson_form.html', {'lesson': instance}, request=request
        )
        response = {
            'lesson_form': lesson_form
        }

        return JsonResponse(response)

    def update(self, request, *args, **kwargs):
        lesson_id = request.data.get('lesson_id')
        instance = self.get_lesson(lesson_id)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)
