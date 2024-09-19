import django_filters
from django import forms
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Value, Q

from services.models import Course


class CourseFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='name_desc_filter', label='Назва складається з')
    price__gte = django_filters.NumberFilter(field_name='full_price', lookup_expr='gte', label='Ціна від:')
    price__lte = django_filters.NumberFilter(field_name='full_price', lookup_expr='lte', label='Ціна до:')
    have_certificate = django_filters.BooleanFilter(method='have_certificate_filter', widget=forms.CheckboxInput,
                                                    label='З сертифікатом')
    is_free = django_filters.BooleanFilter(method='is_free_filter', widget=forms.CheckboxInput,
                                           label='Безкоштовні курси')
    language = django_filters.ChoiceFilter(choices=Course.LANG_CHOICES, label='Мова', empty_label='Будь-яка мова')
    difficulty = django_filters.ChoiceFilter(
        choices=Course.DIFFICULTY_CHOICES,
        label='Рівень',
        empty_label='Все'  # Показывать "Все" как опцию по умолчанию
    )
    owner = django_filters.CharFilter(field_name='owner__id', lookup_expr='icontains', label='Власник:')
    status = django_filters.ChoiceFilter(method='status_filter',choices=[(0, 'Всі'),(1, 'Опублікувані'), (2, 'Чернетки'),], widget=forms.Select,
                                               label='Опублікувати')

    def status_filter(self, queryset, name, value):
        if value == '1':
            return queryset.filter(is_published=True)
        if value == '2':
            return queryset.filter(is_published=False)
        return queryset
    def name_desc_filter(self, queryset, name, value):
        if value.isdigit() and len(value) <= 5:
            return queryset.filter(id=value)

        vector = SearchVector('course_name', 'description')
        query = SearchQuery(value)
        normalization = Value(2).bitor(Value(4))
        qs = queryset.annotate(rank=SearchRank(vector, query, normalization=normalization)).filter(
            rank__gt=0).order_by("-rank")
        return qs

    def is_free_filter(self, queryset, name, value):
        if value:
            return queryset.filter(full_price=0)
        return queryset

    def have_certificate_filter(self, queryset, name, value):
        if value:
            return queryset.filter(have_certificate=True)
        return queryset

    class Meta:
        model = Course
        fields = []
