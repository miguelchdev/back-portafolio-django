from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BioViewSet, EmailServiceViewSet, PageViewSet,
                    ProjectViewSet, ServiceViewSet, TechnologyViewSet)

router = DefaultRouter()
router.register(r'bio', BioViewSet, basename='api-bio')
router.register(r'projects', ProjectViewSet)
router.register(r'service', ServiceViewSet, basename='api-service')
router.register(r'technology', TechnologyViewSet, basename='api-technologys')
router.register(r'email_service', EmailServiceViewSet,
                basename='api-email-service')
router.register(r'page', PageViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
