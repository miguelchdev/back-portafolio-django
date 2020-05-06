from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .serializers import *
from .models import Bio, Project, Service, Technology
from rest_framework import permissions
from rest_framework.response import Response
from .task import send_email


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


class EmailServiceViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmailSerializer

    def create(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            from_email = serializer.validated_data.get('from_email')
            to_email = serializer.validated_data.get('to_email')
            reply_to = serializer.validated_data.get('reply_to')
            body = serializer.validated_data.get('body')
            subject = serializer.validated_data.get('subject')
            send_email(from_email, to_email, body, subject, reply_to)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
