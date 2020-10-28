from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django .http import HttpResponseRedirect
from django .urls import reverse

# Create your views here.

def index (request):
    """Strona główna aplikacji learning log."""
    return render(request, 'learning_logs_app/index.html')

def topics (request):
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

def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla określonego tematu"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz
        form = EntryForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetowrzyć
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect (reverse('learning_logs_app:topic', args=[topic_id]))
            context = {'topic': topic, 'form': form}
            return render (request, 'learning_logs_app/new_entry.html', context)
