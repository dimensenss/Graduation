from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import *


from services.models import Course
from teach.forms import CourseCreateForm
from teach.mixins import OwnerPermissionMixin

class TeachPromoView(TemplateView):
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.:
    #         return redirect('accounts:login')
    #     return super().dispatch(request, *args, **kwargs)

    template_name = 'teach/teach_promo.html'

class TeachCoursesView(LoginRequiredMixin,CreateView):
    template_name = 'teach/teach_courses.html'
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('teach:courses')

    def form_valid(self, form):
        messages.success(self.request, f'Курс {form.instance.course_name} створено')
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_courses'] = Course.objects.filter(owner=self.request.user).select_related('owner')
        return context

class TeachCourseEdit(LoginRequiredMixin,OwnerPermissionMixin, UpdateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'teach/teach_courses.html'
    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs['pk'])

