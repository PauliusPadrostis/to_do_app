from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import TodoItemForm
from django.http import JsonResponse, HttpResponseRedirect


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


class DeleteTodoView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True,})


class UpdateTodoView(generic.UpdateView):
    model = Task
    # fields = ['task', 'due_date', 'status']
    success_url = reverse_lazy('tasks')
    template_name = 'edit_todo.html'
    form_class = TodoItemForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context



