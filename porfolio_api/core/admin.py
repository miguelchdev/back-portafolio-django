from django.contrib import admin
from .models import Bio,Job,School
# Register your models here.

class JobInline(admin.StackedInline):
    model = Job


class SchoolInline(admin.StackedInline):
    model = School

class BioAdmin(admin.ModelAdmin):
    inlines = [SchoolInline,JobInline]

admin.site.register(Bio,BioAdmin)

