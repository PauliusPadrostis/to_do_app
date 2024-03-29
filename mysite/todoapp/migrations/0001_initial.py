# Generated by Django 5.0.1 on 2024-01-26 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200, verbose_name='Task')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Task created')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Due on')),
                ('status', models.CharField(choices=[('td', 'To do'), ('ip', 'In Progress'), ('ca', 'Cancelled'), ('co', 'Completed')], default='td', help_text='Task status', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
