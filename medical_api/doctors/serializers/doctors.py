from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from doctors.models import Doctor
from users.serializers import UserModelSerializer


class ReadDoctorSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    major = StringRelatedField()
    center = StringRelatedField()


    class Meta:
        model = Doctor
        exclude = ['modified', 'created']


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    @staticmethod
    def validate_availability(data):

        if data.seconds < 10800:
            raise serializers.ValidationError("doctor's availability must be greater than 3 hours")

        return data


