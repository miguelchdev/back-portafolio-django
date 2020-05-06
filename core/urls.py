from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BioViewSet, ProjectViewSet, ServiceViewSet, TechnologyViewSet, EmailServiceViewSet

router = DefaultRouter()
router.register(r'bio', BioViewSet, basename='api-bio')
router.register(r'projects', ProjectViewSet)
router.register(r'service', ServiceViewSet, basename='api-service')
router.register(r'technology', TechnologyViewSet, basename='api-technologys')
router.register(r'email_service', EmailServiceViewSet,
                basename='api-email-service')

urlpatterns = [
    path("", include(router.urls)),
]
