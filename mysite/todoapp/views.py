from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import TodoItemForm
from django.http import JsonResponse
from django.contrib.auth import logout,  login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages

# Create your views here.


class LandingPageView(generic.TemplateView):
    template_name = 'index.html'


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Task.COMPLETION_STATUS
        return context

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@login_required
def add_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
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


def custom_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, log the user in after registration
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')  # Redirect to a desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})




