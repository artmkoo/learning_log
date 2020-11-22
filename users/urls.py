"""Defines URL patterns for users"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #include default auth utls
    path('', include('django.contrib.auth.urls')),
]