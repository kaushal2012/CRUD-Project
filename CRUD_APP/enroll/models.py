from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=70)
