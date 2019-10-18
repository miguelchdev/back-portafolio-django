from django.contrib import admin
from .models import Bio, Job, School, Image, Project,Technology,Skill,Contact
from parler.admin import TranslatableAdmin,TranslatableStackedInline,TranslatableTabularInline
# Register your models here.


class JobInline(TranslatableStackedInline):
    model = Job


class ContactInline(admin.TabularInline):
    model = Contact

class ImageInline(admin.StackedInline):
    model = Image


class SkillInline(admin.StackedInline):
    model = Skill


class TechnologyInline(admin.TabularInline):
    model = Technology

class SchoolInline(TranslatableStackedInline):
    model = School


class BioAdmin(TranslatableAdmin):
    inlines = [ContactInline,SkillInline,SchoolInline, JobInline]


class ProjectAdmin(TranslatableAdmin):
    inlines = [TechnologyInline,ImageInline]


admin.site.register(Bio, BioAdmin)
admin.site.register(Project, ProjectAdmin)
