# from rest_framework import serializers
# from .models import CustomUser, Book, Borrow

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'birthdate', 'profile_picture']

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

# class BorrowSerializer(serializers.ModelSerializer):
#     user = CustomUserSerializer(read_only=True)  # Nested user data
#     book = BookSerializer(read_only=True)

#     class Meta:
#         model = Borrow
#         fields = '__all__'
from rest_framework import serializers
from .models import CustomUser, Book, Borrow

# Serializer for CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'birthdate', 'profile_picture']

# Serializer for Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'category', 'published_date', 'description', 'available']

# Serializer for Borrow
class BorrowSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    book = BookSerializer()

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']
