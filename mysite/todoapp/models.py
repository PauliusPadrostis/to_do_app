from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    task = models.CharField(verbose_name='Task', max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='Task created', auto_now_add=True)
    due_date = models.DateField(verbose_name='Due on', blank=True, null=True)

    COMPLETION_STATUS = (
        ('td', 'To do'),
        ('ip', 'In Progress'),
        ('ca', 'Cancelled'),
        ('co', 'Completed'),
    )
    status = models.CharField(max_length=2, choices=COMPLETION_STATUS, default='td', help_text='Task status')

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
