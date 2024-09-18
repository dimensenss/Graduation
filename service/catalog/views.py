from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView, TemplateView
from django_filters.views import FilterView
from rest_framework.views import APIView

from catalog.utils import CourseFilter
from services.models import Course, Category


class CatalogMainView(ListView):
    template_name = 'catalog/catalog_main.html'
    model = Category
    context_object_name = 'cats'

    def get_queryset(self):
        return Category.objects.filter(parent__title='Promo',).only('id', 'title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET, queryset=Course.objects.filter(is_published=True).select_related('owner'))
        return context

class CatalogListView(ListView):
    template_name = 'catalog/catalog_list.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        courses = Course.objects.filter(is_published=True).select_related('owner')
        filtered_qs = CourseFilter(self.request.GET, queryset=courses)
        return filtered_qs.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(self.request.GET, queryset=self.get_queryset())
        return context

class SearchView(TemplateView):
    template_name = 'catalog/includes/courses_list.html'
    def get(self, request, *args, **kwargs):
        courses = Course.objects.filter(is_published=True).select_related('owner')
        filtered_qs = CourseFilter(self.request.GET, queryset=courses)

        context = {'courses': filtered_qs.qs}
        html = render_to_string(self.template_name, context)
        return JsonResponse(html, safe=False)



class GetCoursesView(TemplateView):
    template_name = 'catalog/includes/courses_slider.html'

    def get(self, request, *args, **kwargs):
        cat_id = request.GET.get('cat_id')
        courses = Course.objects.filter(cat_id=cat_id, is_published=True).select_related('owner').order_by('-created_at')

        context = {'courses': courses, 'cat_id': cat_id}
        html = render_to_string(self.template_name, context)
        return JsonResponse(html, safe=False)