# Generated by Django 5.0.1 on 2024-01-27 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]