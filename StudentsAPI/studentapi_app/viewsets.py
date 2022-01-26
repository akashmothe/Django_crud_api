from rest_framework import viewsets
from . import models
from . import serializers


class StudentsViewsets(viewsets.ModelViewSet):
    queryset = models.StudentsDetail.objects.all()
    serializer_class = serializers.StudentSerializer
