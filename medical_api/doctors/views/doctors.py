"""Users views."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Models
from doctors.models import Doctor
from doctors.serializers.doctors import ReadDoctorSerializer, GeneralSerializer


class DoctorViewSet(ModelViewSet):
    """Doctors view set."""
    queryset = Doctor.objects.all()

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == 'create':
            return GeneralSerializer
        if self.action == 'update':
            return GeneralSerializer
        return ReadDoctorSerializer



