from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BioViewSet

router = DefaultRouter()
router.register(r'bio',BioViewSet)
urlpatterns = [
    path("", include(router.urls))
]
