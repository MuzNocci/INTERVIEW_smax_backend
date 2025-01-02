from django.urls import path
from todo.views import ToDoListAndAdd, ToDoEdit, ToDoDelete



urlpatterns = [

    path('', ToDoListAndAdd.as_view(), name='list'),
    path('task/edit/<uuid:id>', ToDoEdit.as_view(), name='edit'),
    path('task/delete/<uuid:id>', ToDoDelete.as_view(), name='delete'),
    
]