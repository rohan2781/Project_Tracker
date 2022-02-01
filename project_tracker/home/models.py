from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
