from django.db import models

# Create your models here.

# my first model from book Python - instr for programer

class Topic (models.Model):
    '''Temat poznawany przez uzytkownika'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        '''Zwraca reprezentacje modelu w postaci ciagu tekstowego.'''
        return self.text