from django.db import models

class Developer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
