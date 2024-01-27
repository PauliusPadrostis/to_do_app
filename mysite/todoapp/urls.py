from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('accounts/', include('django.contrib.auth.urls')),
]