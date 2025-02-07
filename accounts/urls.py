from django.urls import path
from .views import LoginView,CustomUserListCreateView, CustomUserDetailView
from . import views

urlpatterns = [
    # path('register/', views.register, name='register')
    path('users/', CustomUserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'), 

]
