"""User models admin."""

# Django
from django.contrib import admin

# Models
from doctors.models import Doctor, Major, Center


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Doctor model admin."""

    list_display = ('first_name', 'last_name', 'biography', 'major',)
    search_fields = ('last_name', 'major')
    list_filter = ('major', 'last_name')


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    """Doctor model admin."""

    list_display = ('name', 'description',)


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    """Doctor model admin."""

    list_display = ('name', 'location',)
