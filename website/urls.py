
# In website/urls.py

from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home),  # Root URL, point to the home view
    path('api/', include('accounts.urls')), 
    path('api/', include('library_system.urls')),
]
