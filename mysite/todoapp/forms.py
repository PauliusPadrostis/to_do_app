from django import forms
from .models import Task


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due_date', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the status field widget to use a select input
        self.fields['status'].widget = forms.Select(attrs={'class': 'form-control'})