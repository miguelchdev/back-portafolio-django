from rest_framework import serializers
from .models import *
from drf_queryfields import QueryFieldsMixin
from versatileimagefield.serializers import VersatileImageFieldSerializer

class BioSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    pic = VersatileImageFieldSerializer(sizes='responsive_sizes')
    class Meta:
        model = Bio
        fields = ('name','last_name','role' ,'about','welcome_message','pic')
   
