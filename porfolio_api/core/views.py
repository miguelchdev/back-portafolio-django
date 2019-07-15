from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Bio
# Create your views here.


class BioViewSet(viewsets.ModelViewSet):
    serializer_class = BioSerializer
    queryset = Bio.objects.all()
