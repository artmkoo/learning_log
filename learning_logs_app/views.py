from django.shortcuts import render

# Create your views here.

def index (request):
    """Strona główna aplikacji learning log."""
    return render(request, 'learning_logs_app/index.html')