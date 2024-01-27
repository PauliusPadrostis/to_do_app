from django.shortcuts import render
from django.views import generic
from .models import *


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'
