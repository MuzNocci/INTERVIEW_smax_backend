from django.urls import path
from todo.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
