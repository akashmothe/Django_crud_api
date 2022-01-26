from django.db import models

# Create your models here.
class StudentsDetail(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_edu = models.CharField(max_length=50)
    stud_age = models.IntegerField()
    
