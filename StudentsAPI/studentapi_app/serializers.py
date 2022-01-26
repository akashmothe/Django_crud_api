from dataclasses import field
from rest_framework import serializers
from .models import StudentsDetail

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsDetail
        fields = '__all__'
