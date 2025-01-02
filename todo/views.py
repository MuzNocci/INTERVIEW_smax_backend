from django.shortcuts import render
from django.views import View



class HomeView(View):

    def get(self, request):

        context = {
            'title':'To do list'
        }
        return render(request, 'todo.view.html', context)