from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='index'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_todo/', views.add_todo_item, name='add_todo'),
    path('delete_todo/<int:pk>/delete', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('update_todo/<int:pk>/update', views.UpdateTodoView.as_view(), name='update_todo'),
]