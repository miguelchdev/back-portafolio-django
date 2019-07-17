from rest_framework import serializers
from .models import *
from drf_queryfields import QueryFieldsMixin
from versatileimagefield.serializers import VersatileImageFieldSerializer


class JobSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','employer','title','description','location','start_date','end_date')

class SchoolSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','location','degree','start_date','end_date','url')

class BioSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    pic = VersatileImageFieldSerializer(sizes='responsive_sizes')
    jobs = JobSerializer(many=True)
    education = SchoolSerializer(many=True)
    class Meta:
        model = Bio
        fields = ('id','name','last_name','role' ,'about','welcome_message','pic','education','jobs')
   
