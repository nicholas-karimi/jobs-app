from django.urls import path, include 

from .views import notifications

urlpatterns = [
    path('add/', notifications, name='notifications'),
]