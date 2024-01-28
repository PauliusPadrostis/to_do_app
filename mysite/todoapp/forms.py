from django import forms
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due_date', 'status']
        widgets = {'due_date': DateInput()}

