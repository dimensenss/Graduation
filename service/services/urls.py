from django.urls import path
from .views import *


app_name = 'services'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),


]