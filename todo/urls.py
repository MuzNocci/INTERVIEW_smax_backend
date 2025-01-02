from django.urls import path
from todo.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
