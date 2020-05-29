from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Bio, Job, School, Image, Project, Technology, Skill, Contact, Service
from parler.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline
# Register your models here.


class JobInline(TranslatableStackedInline):
    model = Job


class ContactInline(admin.TabularInline):
    model = Contact


class ImageInline(admin.StackedInline):
    model = Image
    fields = ('file', 'alt')


class SkillInline(admin.StackedInline):
    model = Skill


class TechnologyAdmin(admin.ModelAdmin):
    model = Technology


class SchoolInline(TranslatableStackedInline):
    model = School


class BioAdmin(TranslatableAdmin):
    inlines = [ContactInline, SkillInline, SchoolInline, JobInline]


class ProjectAdmin(TranslatableAdmin):
    inlines = [ImageInline]
    filter_horizontal = ['technologys']


class ServiceAdmin(TranslatableAdmin):
    model = Service


admin.site.register(Bio, BioAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Technology, TechnologyAdmin)
