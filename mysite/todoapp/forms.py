from django import forms
from .models import Task


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due_date',]