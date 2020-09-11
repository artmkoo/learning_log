from django.shortcuts import render
# import dla topics
from .models import Topic

# Create your views here.

def index (request):
    """Strona główna aplikacji learning log."""
    return render(request, 'learning_logs_app/index.html')

def topics (request):
    """Wyświetlanie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)