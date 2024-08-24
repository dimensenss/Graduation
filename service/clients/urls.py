from django.urls import path
from .views import *


app_name = 'clients'

urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='register'),
    path('activate/<str:uid>/<str:token>/', ActivateClientView.as_view(), name='activate'),

]