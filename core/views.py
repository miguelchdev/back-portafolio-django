from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import Bio, Page, Project, Service, Technology
from .serializers import *
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


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Page.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {obj.pop('identifier'): obj for obj in serializer.data}
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
