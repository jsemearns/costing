from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)