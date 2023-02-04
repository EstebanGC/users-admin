from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Type a title'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type a description'}),
        #     'important': forms.CheckBoxInput(attrs={'class': 'form-check-input m-auto'})
        # }