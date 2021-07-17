from django.urls import path, re_path

from . import views
app_name = 'tasks_app'

urlpatterns = [
    path (
        'api/task/create/',
          views.TaskCreateApiView.as_view(), 
          name='createTask'
    ),
    path (
        'api/task/incomplete/',
          views.TaskIncompleteApiView.as_view(), 
          name='taskIncomplete'
    ),
    path (
        'api/task/complete/',
          views.TaskCompleteApiView.as_view(), 
          name='tasComplete'
    ),
    path (
        'api/task/update/<pk>/',
          views.TaskUpdateView.as_view(), 
          name='tasComplete'
    ),

]