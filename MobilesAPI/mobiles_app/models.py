from pyexpat import model
from django.db import models

# Create your models here.
class MobilesDetail(models.Model):
    mob_model = models.CharField(max_length=100)
    mob_ram = models.CharField(max_length=10)
    mob_rom = models.CharField(max_length=10)
    price = models.IntegerField()
