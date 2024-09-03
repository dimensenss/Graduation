from django.urls import path
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('', CatalogMainView.as_view(), name='catalog'),
    path('search/', SearchView.as_view(), name='search'),
    path('api/v1/get-courses/', GetCoursesView.as_view(), name='get_courses'),
]
