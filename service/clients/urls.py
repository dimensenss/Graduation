from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from .views import *

app_name = 'clients'

urlpatterns = [
    path('register/', RegisterClientView.as_view(), name='register'),
    path('login/', ClientLoginView.as_view(), name='login'),
    path('profile/', ClientProfileView.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

]

