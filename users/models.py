from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Departments(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='datauser')
    email = models.EmailField(max_length = 40)
    department = models.TextField(default='')

    def __str__(self):
        return self.email