from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here
class Users(models.Model):
    email = models.EmailField(max_length = 40)
    password = models.CharField(max_length = 200)
    department = models.TextField(default='')
    isAdmin = models.IntegerField(default=0)