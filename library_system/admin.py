from django.contrib import admin
from .models import CustomUser, Book, Borrow

# Customizing the User Admin Panel
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('user_type', 'is_active', 'is_staff')

# Customizing the Book Admin Panel
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'published_date', 'available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('available', 'category')

# Customizing the Borrow Admin Panel
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    search_fields = ('user__username', 'book__title')
    list_filter = ('status', 'borrow_date')

# Register models in Django Admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)

# Customizing the Admin Panel Headers
admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Admin Panel"
admin.site.index_title = "Library Dashboard"
