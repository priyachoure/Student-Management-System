from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT')
    )
    user_type = models.CharField(max_length=50, choices=USER, default=1)
    user_profile = models.ImageField(upload_to='media/profile_pic')
