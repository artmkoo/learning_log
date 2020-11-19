from django import forms

from .models import Topic, Entry

class TopicForm (forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Mata:
        model = Entry
        fields = ['text']
        labels = {'text': ''} # niby ma byc blank label ...? a w kodzie jest 
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}