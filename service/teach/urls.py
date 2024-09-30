from django.urls import path
from rest_framework import routers

from teach.modules import TeachCourseModulesView, CreateModuleAPI
from teach.views import *

app_name = 'teach'


router = routers.SimpleRouter()
router.register('api/v1/course_edit_info', UpdateCourseView)
router.register('api/v1/course_edit_content', CreateModuleAPI)



urlpatterns = [
    path('', TeachPromoView.as_view(), name='teach_promo'),
    path('courses/', TeachCoursesView.as_view(), name='courses'),
    path('courses/new/', TeachCourseCreate.as_view(), name='create_course'),
    path('courses/edit-info/<int:pk>/', TeachCourseInfoEditView.as_view(), name='course_edit_info'),
    path('courses/edit-content/<int:pk>/', TeachCourseModulesView.as_view(), name='course_edit_content'),
    path('courses/edit-content/<int:pk>/', TeachCourseModulesView.as_view(), name='course_edit_content'),

    path('api/v1/teach-search/', TeachCoursesSearchView.as_view(), name='course_search'),
]+router.urls