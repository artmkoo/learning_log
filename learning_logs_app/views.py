from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm
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
    """Wyświetla pojedyńczy temat i wszystkie powiazane z nim wpisy
    Show a single topic and all its entries."""   
    topic = Topic.objects.get (id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render (request, 'learning_logs_app/topic.html', context)

def new_topic(request):
    """Dodaj nowy temat - Add a new topic """
    if request.method != 'POST':
        #Nie przekazano żadnych danych, nalezy utworzyć pusty formularz
        form = TopicForm()
    else:
        #Przkazano dane za pomoca żadania POST, należy je prztworzyć
        form = TopicForm (data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs_app:topics')

    # Display a blank or invalid form.        
    context = {'form':form}
    return render (request, 'learning_logs_app/new_topic.html', context)

def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla określonego tematu - Add a new entry for a particular topic"""
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
            return redirect ('learning_logs_app:topic', topic_id=topic_id)

            # Display a blank or invalid form.
            context = {'topic': topic, 'form': form}
            return render (request, 'learning_logs_app/new_entry.html', context)
