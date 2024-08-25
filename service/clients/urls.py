from django.urls import path
from .views import *


app_name = 'clients'

urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

]