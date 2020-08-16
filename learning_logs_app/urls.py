""" Definiuje wzorce adresów URL dla aplikacji learning_logs_app"""
from django.urls import path
from . import views

app_name = 'learning_logs_app'
urlpatterns = [
    # Strona glówna 
    path('', views.index, name='index'),
]