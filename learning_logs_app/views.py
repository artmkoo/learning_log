from django.shortcuts import render
<<<<<<< HEAD
# import dla topics
from .models import Topic
=======
from .models import Topic
from .forms import TopicForm
from django .http import HttpResponseRedirect
from django .urls import reverse
>>>>>>> 9e4d9739c892ec5e14fda86cfabec031709d8bb6

# Create your views here.

def index (request):
    """Strona główna aplikacji learning log."""
    return render(request, 'learning_logs_app/index.html')

def topics (request):
<<<<<<< HEAD
    """Wyświetlanie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
=======
    """ Wyświetlanie wszystkich tematów."""
    topics = Topic.objects.order_by ('date_added')
    context = {'topics':topics}
    return render (request, 'learning_logs_app/topics.html', context)

def topic (request, topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiazane z nim   wpisy"""
    topic = Topic.objects.get (id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render (request, 'learning_logs_app/topic.html', context)

def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != 'POST':
        #Nie przekazano żadnych danych, nalezy utworzyć pusty formularz
        form = TopicForm()
    else:
        #Przkazano dane za pomoca żadania POST, należy je prztworzyć
        form = TopicForm (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs_app:topics'))

    context = {'form':form}
    return render (request, 'learning_logs_app/new_topic.html', context) 
>>>>>>> 9e4d9739c892ec5e14fda86cfabec031709d8bb6
