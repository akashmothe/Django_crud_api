from pyexpat import model
from rest_framework import serializers
from .models import MobilesDetail


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilesDetail
        fields = '__all__'
