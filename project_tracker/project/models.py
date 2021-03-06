from http import client
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from home.models import Client

class Project(models.Model):
    name = models.CharField(max_length=80,default='NULL')
    efforts = models.IntegerField()
    dead_line = models.DateField()
    person= models.CharField(max_length=100,default='NULL')
    developer= models.CharField(max_length=100,default='NULL')
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)

    def __str__(self):
        return (self.name)


class Comment(models.Model):
    name=models.CharField(max_length=20,default='NULL')
    p_id=models.IntegerField()
    feed = models.TextField(blank=False)
    


class Reply(models.Model):
    name=models.CharField(max_length=20,default='NULL')
    c_id=models.IntegerField()
    feed = models.TextField(blank=False)