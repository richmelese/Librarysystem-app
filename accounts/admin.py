from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'birthdate', 'password','profile_picture']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthdate', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birthdate', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

