from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserRegistration(AbstractUser):
    age = models.PositiveBigIntegerField(null = True, blank=True)

#to fix the adding user issue
# def __str__(self):
#     return self.name.username
#TypeError at /admin/accounts/customuserregistration/add/