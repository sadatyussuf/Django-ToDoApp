from os import name
from django import forms
from .models import todoModel
class todoForm(forms.ModelForm):
    class Meta:
        model = todoModel
    
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Make Your List'})
        }
        labels = {
        'name':'',
    }

