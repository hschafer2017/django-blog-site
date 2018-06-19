from django.db import models
from django.contrib.auth.models import User

# Create your models here - ACCOUNTS.

class Photo(models.Model):
    image = models.ImageField(upload_to="avatars", blank=True, null=True)

def __str__(self):
    return self.title