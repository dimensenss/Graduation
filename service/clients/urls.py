from django.urls import path
from .views import *


app_name = 'clients'

urlpatterns = [
    path('check/', ClientViewSet.as_view({'get': 'list'}), name='auth'),
]