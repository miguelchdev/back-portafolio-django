from django.contrib import admin
from .models import Bio, Job, School, Image, Project,Technology,Skill,Contact
# Register your models here.


class JobInline(admin.StackedInline):
    model = Job


class ContactInline(admin.TabularInline):
    model = Contact

class ImageInline(admin.StackedInline):
    model = Image


class SkillInline(admin.StackedInline):
    model = Skill


class TechnologyInline(admin.TabularInline):
    model = Technology

class SchoolInline(admin.StackedInline):
    model = School


class BioAdmin(admin.ModelAdmin):
    inlines = [ContactInline,SkillInline,SchoolInline, JobInline]


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline,ImageInline]


admin.site.register(Bio, BioAdmin)
admin.site.register(Project, ProjectAdmin)
