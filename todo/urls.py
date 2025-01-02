from django.urls import path
from todo.views import TodoView



urlpatterns = [
    path('', TodoView.as_view(), name='home'),
]