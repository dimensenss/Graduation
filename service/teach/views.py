from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import *
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import *
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet

from catalog.utils import CourseFilter
from clients.serializers import ClientSerializer
from services.models import Course, CourseInfo
from teach.forms import CourseCreateForm, CourseUpdateForm, CourseInfoUpdateForm
from teach.mixins import OwnerPermissionMixin
from teach.repositories.course import CourseRepository
from teach.serializers import CourseUpdateSerializer
from teach.services.course import CourseService
import json


class TeachPromoView(TemplateView):
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.:
    #         return redirect('accounts:login')
    #     return super().dispatch(request, *args, **kwargs)

    template_name = 'teach/teach_promo.html'


class TeachCoursesView(LoginRequiredMixin, ListView):
    template_name = 'teach/teach_courses_list.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        courses = Course.objects.filter(owner=self.request.user).only('id', 'course_name', 'preview',
                                                                      'full_price').order_by('-created_at')
        filtered_qs = CourseFilter(self.request.GET, queryset=courses)
        return filtered_qs.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TeachCourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'teach/teach_course_create.html'
    success_url = reverse_lazy('teach:courses')

    def form_valid(self, form):
        messages.success(self.request, f'Курс {form.instance.course_name} створено')
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class TeachCourseEdit(LoginRequiredMixin, OwnerPermissionMixin, DetailView):
    model = Course
    template_name = 'teach/teach_course_edit.html'
    context_object_name = 'course'
    form_class = CourseUpdateForm

    def get_object(self, queryset=None):
        return Course.objects.select_related('owner', 'info').get(pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        course_info = CourseInfo.objects.get_or_create(course=course)[0]

        return render(request, self.template_name, {

            'course': course,
        })


class TeachCoursesSearchView(TemplateView):
    template_name = 'teach/includes/teach_included_courses_list.html'

    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(owner=self.request.user).only('id', 'course_name', 'preview', 'is_published')
        filtered_qs = CourseFilter(self.request.GET, queryset=courses)

        context = {'courses': filtered_qs.qs}
        html = render_to_string(self.template_name, context)
        return JsonResponse(html, safe=False)


class UpdateCourseView(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CourseUpdateSerializer
    queryset = Course.objects.all()
    service = CourseService(CourseRepository())

    def get_object(self):
        return Course.objects.select_related('owner', 'info').get(pk=self.kwargs['pk'])

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            updated_course = self.service.update_course(instance.id, serializer.validated_data)
            return Response(CourseUpdateSerializer(updated_course).data)
        else:
            return Response(serializer.errors, status=400)

    @action(methods=['PUT'], detail=True)
    def update_authors(self, request, *args, **kwargs):
        instance = self.get_object()
        authors = request.data.get('authors')
        try:
            self.service.update_authors(instance.info, authors)
        except ValueError as e:
            return Response({"authors": [str(e)]}, status=400)  # Вернуть ошибку как список
        return JsonResponse({'authors': ClientSerializer(instance.info.authors.all(), many=True).data})
