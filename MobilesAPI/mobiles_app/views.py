from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . serializers import MobileSerializer
from mobiles_app import serializers

# Create your views here.
class MobileViewset(viewsets.ModelViewSet):
    queryset = models.MobilesDetail.objects.all()
    serializer_class = serializers.MobileSerializer
    