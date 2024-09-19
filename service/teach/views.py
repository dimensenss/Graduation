from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import *

from catalog.utils import CourseFilter
from services.models import Course
from teach.forms import CourseCreateForm
from teach.mixins import OwnerPermissionMixin

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
        courses = Course.objects.filter(owner=self.request.user).only('id', 'course_name', 'preview', 'full_price').order_by('-created_at')
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

class TeachCourseEdit(LoginRequiredMixin,OwnerPermissionMixin, UpdateView):
    model = Course
    form_class = CourseCreateForm #CourseUpdateForm
    template_name = 'teach/teach_course_edit.html'
    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs['pk'])

class TeachCoursesSearchView(TemplateView):
    template_name = 'teach/includes/teach_included_courses_list.html'
    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(owner=self.request.user).only('id','course_name', 'preview', 'is_published')
        filtered_qs = CourseFilter(self.request.GET, queryset=courses)

        context = {'courses': filtered_qs.qs}
        html = render_to_string(self.template_name, context)
        return JsonResponse(html, safe=False)

