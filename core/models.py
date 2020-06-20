from cloudinary.models import CloudinaryField
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
    pic = CloudinaryField(null=True, blank=True)

    def __unicode__(self):
        return self.about


class Technology(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Project(TranslatableModel):
    title = models.CharField(max_length=25)
    link = models.URLField()
    translations = TranslatedFields(
        description=models.TextField()
    )
    date = models.DateField()
    technologys = models.ManyToManyField(
        Technology, related_name='technologys')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


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
        degree=models.CharField(max_length=35)
    )
    start_date = models.DateField()
    end_date = models.DateField()
    url = models.URLField()


class Image(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE)
    file = CloudinaryField()
    alt = models.CharField(max_length=50, null=True, blank=True)


class Skill(models.Model):
    bio = models.ForeignKey(Bio, related_name='skills',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=25)


class Contact(models.Model):
    bio = models.ForeignKey(Bio, related_name='contacts',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    link = models.URLField()


class Service(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=25),
        description=models.TextField(max_length=150)
    )


class Page(TranslatableModel):
    identifier = models.CharField(max_length=100)
    translations = TranslatedFields(
        title=models.CharField(max_length=150),
    )

    def __str__(self):
        return self.identifier


class PageContent(TranslatableModel):
    page = models.ForeignKey(
        Page, related_name='page_contents', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)
    translations = TranslatedFields(
        content=models.CharField(max_length=255),
    )


class ImageContent(TranslatableModel):
    page = models.ForeignKey(
        Page, related_name='images', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)
    file = CloudinaryField()
    translations = TranslatedFields(
        alt=models.CharField(max_length=50, null=True, blank=True),
    )
