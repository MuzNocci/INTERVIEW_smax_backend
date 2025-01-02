from django.shortcuts import render
from django.views import View



class TodoView(View):


    def get(self, request):

        context = {
            'title':'ToDO | Sistema de Lista de Tarefas'
        }
        return render(request, 'todo.view.html', context)
    
    
    def post(self, request):

        pass


    def put(self, request):

        pass


    def delete(self, request):

        pass