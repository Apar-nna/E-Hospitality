from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('user', 'patient'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='user')

    def __str__(self):
        return self.username
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'

class LoginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200, default='default_password')  # Set default value
    user_type = models.CharField(max_length=20, choices=CustomUser.USER_TYPE_CHOICES, default='user')

    def __str__(self):
        return self.username
