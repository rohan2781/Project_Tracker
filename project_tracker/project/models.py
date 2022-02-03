from http import client
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from home.models import Client

class Project(models.Model):
    name = models.CharField(max_length=80)
    efforts = models.IntegerField()
    dead_line = models.DateField()
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)

    def __str__(self):
        return (self.name)