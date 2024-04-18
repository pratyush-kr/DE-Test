from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from app import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('chat', views.ChatView)


urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)