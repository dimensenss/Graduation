from django.urls import path

from teach.views import *

app_name = 'teach'





urlpatterns = [
    path('', TeachPromoView.as_view(), name='teach_promo'),
    path('courses/', TeachCoursesView.as_view(), name='courses'),
    path('courses/new/', TeachCourseCreate.as_view(), name='create_course'),
    path('courses/edit-info/<int:pk>/', TeachCourseEdit.as_view(), name='course_edit_info'),
    path('api/v1/course-edit-info/<int:pk>/', UpdateCourseView.as_view(), name='api_course_edit_info'),
    path('api/v1/teach-search/', TeachCoursesSearchView.as_view(), name='course_search'),
]