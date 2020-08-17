""" Definiuje wzorce adresów URL dla aplikacji learning_logs_app"""
from django.urls import path
from . import views

app_name = 'learning_logs_app' # nie wiem po co to ale jak zakomentuje to tez dziala :)
urlpatterns = [
    # Strona glówna 
    path('', views.index, name='index'),
    #strona tematów - topicShow all topics
    path('topics/', views.topics, name='topics'),
]