from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BioViewSet,ProjectViewSet,ServiceViewSet

router = DefaultRouter()
router.register(r'bio',BioViewSet,basename='api-bio')
router.register(r'projects', ProjectViewSet)
router.register(r'service', ServiceViewSet,basename='api-bio')
urlpatterns = [
    path("", include(router.urls))
]
