from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.


class Bio(TranslatableModel):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    translations = TranslatedFields(
        about=models.TextField(),
        welcome_message=models.TextField(), role=models.CharField(max_length=25)
    )
    pic = VersatileImageField(ppoi_field='ppoi')
    ppoi = PPOIField('pic_ppoi')

    def __unicode__(self):
        return self.about


class Project(TranslatableModel):
    title = models.CharField(max_length=25)
    link = models.URLField()
    translations = TranslatedFields(
        description=models.TextField()
    )
    date = models.DateField()


class Job(TranslatableModel):
    bio = models.ForeignKey(Bio, related_name='jobs', on_delete=models.CASCADE)
    employer = models.CharField(max_length=35)
    translations = TranslatedFields(
        title=models.CharField(max_length=25),
        description=models.TextField()
    )
    location = models.CharField(max_length=80)
    start_date = models.DateField()
    end_date = models.DateField()


class School(TranslatableModel):
    bio = models.ForeignKey(
        Bio, related_name='education', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    translations = TranslatedFields(
        degree = models.CharField(max_length=35)
    )
    start_date = models.DateField()
    end_date = models.DateField()
    url = models.URLField()


class Technology(models.Model):
    project = models.ForeignKey(
        Project, related_name='technologys', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)


class Image(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE)
    file = VersatileImageField(ppoi_field='ppoi')
    ppoi = PPOIField('image_ppoi')


class Skill(models.Model):
    bio = models.ForeignKey(Bio, related_name='skills',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=25)


class Contact(models.Model):
    bio = models.ForeignKey(Bio, related_name='contacts',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    link = models.URLField()
