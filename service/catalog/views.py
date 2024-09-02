from django.shortcuts import render
from django.views.generic import ListView

from services.models import Course


class CatalogMainView(ListView):
    template_name = 'catalog/catalog_main.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchView(ListView):
    queryset = Course.objects.all()
    template_name = 'catalog/catalog.html'
    context_object_name = 'courses'
    allow_empty = True
    courses_filter = None

    # def get_template_names(self):
    #     if self.request.htmx:
    #         return 'includes/products_list.html'
    #     return self.template_name

    # def get_queryset(self):
    #     queryset = super().get_queryset().annotate(
    #         sneakers_first_image=F("first_image__image"))
    #     self.sneakers_filter = SneakersFilter(self.request.GET, queryset=queryset)
    #     queryset = self.sneakers_filter.qs
    #
    #     return queryset
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(filter=self.sneakers_filter)
    #     context['is_search_page'] = True
    #
    #     return dict(list(context.items()) + list(c_def.items()))

