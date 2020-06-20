from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from parler.admin import (TranslatableAdmin, TranslatableStackedInline,
                          TranslatableTabularInline)

from .models import (Bio, Contact, Image, ImageContent, Job, Page, PageContent,
                     Project, School, Service, Skill, Technology)

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


class PageContentInline(TranslatableStackedInline):
    model = PageContent


class ImageContentInline(TranslatableStackedInline):
    model = ImageContent


class PageAdmin(TranslatableAdmin):
    inlines = [PageContentInline, ImageContentInline]


admin.site.register(Bio, BioAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Page, PageAdmin)
