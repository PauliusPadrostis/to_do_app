from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import TodoItemForm
from django.http import JsonResponse


# Create your views here.

class LandingPageView(generic.TemplateView):
    template_name = 'index.html'


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Task.COMPLETION_STATUS
        return context


def add_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return JsonResponse({'success': True, 'task_id': task.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = TodoItemForm()

    return render(request, 'tasklist.html', {'form': form})


