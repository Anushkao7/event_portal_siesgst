from rest_framework.routers import DefaultRouter
from myfirstapp.api.urls import post_router
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.registry.extend(post_router.registry)

urlpatterns = [
    path('', include('myfirstapp.api.urls')),  # Include your app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
