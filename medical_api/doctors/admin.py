"""User models admin."""

# Django
from django.contrib import admin

# Models
from doctors.models import Doctor, Major, Center


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Doctor model admin."""

    list_display = ('user', 'biography', 'major',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name',)
    list_filter = ('major', 'center')


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    """Doctor model admin."""

    list_display = ('name', 'description',)


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    """Doctor model admin."""

    list_display = ('name', 'location',)
