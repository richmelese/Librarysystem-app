from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # User roles: Admin, Librarian, Member
    USER_TYPES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='member')

    # Avoid group conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='library_customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='library_customuser_permissions',
        blank=True
    )

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)  # Unique ISBN for each book
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    published_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Borrow(models.Model):
    STATUS_CHOICES = (
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} ({self.status})"
