from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BioViewSet,ProjectViewSet

router = DefaultRouter()
router.register(r'bio',BioViewSet,basename='api-bio')
router.register(r'projects', ProjectViewSet)
urlpatterns = [
    path("", include(router.urls))
]
