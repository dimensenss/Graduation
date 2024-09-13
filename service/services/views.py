
from django.views.generic import ListView, DetailView

from services.models import Course



class CourseDetailView(DetailView):
    model = Course
    template_name = 'services/course_detail.html'
    context_object_name = 'course'

    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(ListView):
    template_name = 'services/index.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
