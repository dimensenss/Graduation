from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from clients.views import SendActivationEmailView
from services.views import CoursesAPIView
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

router = SimpleRouter()
router.register('courses', CoursesAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/', include('allauth.urls')),

    path('', include('services.urls', namespace='services')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('api/send_activation_email/', SendActivationEmailView.as_view(), name='send_activation_email_api'),

]+ debug_toolbar_urls()

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
