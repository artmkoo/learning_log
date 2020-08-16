""" Definiuje wzorce adresów URL dla aplikacji learning_logs_app"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Strona glówna 
    url(r'^$', views.index, name='index'),
]