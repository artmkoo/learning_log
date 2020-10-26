""" Definiuje wzorce adresów URL dla aplikacji learning_logs_app"""
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'learning_logs_app' # nie wiem po co to ale jak zakomentuje to tez dziala :)
urlpatterns = [
    # Strona glówna - Home page
    path('', views.index, name='index'),

    #strona tematów - topic - Show all topics
    path('topics/', views.topics, name='topics'),

    #strona poszczegolnych tematow / Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic')
]