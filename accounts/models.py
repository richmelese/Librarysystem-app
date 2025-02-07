from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator # check the email correct format

class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    REQUIRED_FIELDS = ['email'] 
    
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address.")])

    def __str__(self):
        return self.username


