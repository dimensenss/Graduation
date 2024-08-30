
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from clients.views import SendActivationEmailView
from services.views import CoursesAPIView

router = SimpleRouter()
router.register('courses', CoursesAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('', include('services.urls', namespace='services')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('api/send_activation_email/', SendActivationEmailView.as_view(), name='send_activation_email_api'),
]

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)