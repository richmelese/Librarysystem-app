from rest_framework import serializers
from .models import CustomUser
from django.core.exceptions import ValidationError 

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'birthdate', 'password','profile_picture']

def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Check if the email is already in use
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        
        return email