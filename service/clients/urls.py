from django.urls import path
from .views import *


app_name = 'clients'

urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),


]