from rest_framework import serializers
from .models import *
from drf_queryfields import QueryFieldsMixin
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedField, TranslatedFieldsField


class JobSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'employer', 'title', 'description',
                  'location', 'start_date', 'end_date')


class SchoolSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'location', 'degree',
                  'start_date', 'end_date', 'url')


class SkillSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')


class ContactListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data

        return {
            item.name: item.link for item in iterable
        }


class ContactSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'link')
        list_serializer_class = ContactListSerializer


class BioSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    jobs = JobSerializer(many=True, required=False)
    education = SchoolSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    role = serializers.CharField()
    social_networks = ContactSerializer(
        many=True, required=False, source='contacts')

    class Meta:
        model = Bio
        fields = ('id', 'pic', 'name', 'last_name', 'role', 'about', 'welcome_message',
                  'pic', 'social_networks', 'skills', 'education', 'jobs')


class ImageSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    file = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('id', 'file', 'alt')


class TechnologyListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data

        return [
            item.name for item in iterable
        ]


class TechnologySerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name')
        list_serializer_class = TechnologyListSerializer


class ProjectSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)
    technologys = TechnologySerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'date',
                  'link', 'images', 'technologys')


class ServiceSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'description')


class EmailSerializer(serializers.Serializer):
    to_email = serializers.EmailField(required=True)
    from_email = serializers.EmailField(required=True)
    reply_to = serializers.EmailField(required=False)
    body = serializers.CharField(required=True)
    subject = serializers.CharField(max_length=200)
