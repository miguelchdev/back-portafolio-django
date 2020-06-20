from drf_queryfields import QueryFieldsMixin
from parler_rest.fields import TranslatedField, TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from .models import *


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
    pic = serializers.ImageField()
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


class ObjectListSerializer(serializers.ListSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'key_field' arg up to the superclass
        key_field = kwargs.pop('key_field', 'id')
        # Instantiate the superclass normally
        super(ObjectListSerializer, self).__init__(*args, **kwargs)
        self.key_field = key_field

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        return {
            getattr(item, self.key_field): self.child.to_representation(item) for item in iterable
        }


class ImageContentSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    file = serializers.ImageField()

    @ classmethod
    def many_init(cls, *args, **kwargs):
        # Instantiate the child serializer.
        kwargs['child'] = cls()
        # Instantiate the parent list serializer.
        return ObjectListSerializer(*args, **kwargs)

    class Meta:
        model = ImageContent
        fields = ('id', 'file', 'alt')


class PageContentSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    @ classmethod
    def many_init(cls, *args, **kwargs):
        # Instantiate the child serializer.
        kwargs['child'] = cls()
        # Instantiate the parent list serializer.
        return ObjectListSerializer(*args, **kwargs)

    def to_representation(self, instance):
        return instance.content

    class Meta:
        model = PageContent
        fields = ('content',)


class PageSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    images = ImageContentSerializer(many=True, key_field="identifier")
    page_contents = PageContentSerializer(many=True, key_field="identifier")

    class Meta:
        model = Page
        fields = ('id', 'title', 'identifier', 'images', 'page_contents')
