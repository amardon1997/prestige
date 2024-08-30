from django.db import models
from django.contrib.auth.models import User


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    
class Resume(models.Model):
    file_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    key_skills = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name