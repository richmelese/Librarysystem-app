# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import UserCreateView, BookListCreateView, BookDetailView, BorrowBookView

# urlpatterns = [
#     path('register/', UserCreateView.as_view(), name='user-register'),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
#     path('books/', BookListCreateView.as_view(), name='book-list'),
#     path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
#     path('books/borrow/', BorrowBookView.as_view(), name='borrow-book'),
# ]



from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    UserListCreateView, UserDetailView,
    BookListCreateView, BookDetailView,
    BorrowListCreateView, BorrowDetailView,CategoryListCreateView, CategoryDetailView
    
)

urlpatterns = [
    # User API Endpoints
    # path('users/', UserListCreateView.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Book API Endpoints
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Borrow API Endpoints
    path('borrows/', BorrowListCreateView.as_view(), name='borrow-list'),
    path('borrows/<int:pk>/', BorrowDetailView.as_view(), name='borrow-detail'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
