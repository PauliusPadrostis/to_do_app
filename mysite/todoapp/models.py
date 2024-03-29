from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Task(models.Model):
    task = models.CharField(verbose_name='Task', max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='Task created', auto_now_add=True)
    due_date = models.DateField(verbose_name='Due on', blank=True, null=True)

    COMPLETION_STATUS = (
        ('td', 'To do'),
        ('ip', 'In Progress'),
        ('ca', 'Cancelled'),
        ('co', 'Completed'),
    )
    status = models.CharField(max_length=2, choices=COMPLETION_STATUS, default='td')

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('tasks')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
