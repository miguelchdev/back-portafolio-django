from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Bio, Project, Service, Technology
from rest_framework import permissions
# Create your views here.


class BioViewSet(viewsets.ModelViewSet):
    serializer_class = BioSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Bio.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Project.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Service.objects.all()


class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Technology.objects.all()
