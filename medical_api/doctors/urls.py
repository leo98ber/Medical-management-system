"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from doctors.views.doctors import DoctorViewSet


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = [
    path('', include(router.urls))
]
