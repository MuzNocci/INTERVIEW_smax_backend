from django.shortcuts import render
from django.views import View



class TodoView(View):


    def get(self, request):

        context = {
            'title':'To do list'
        }
        return render(request, 'todo.view.html', context)
    
    
    def post(self, request):

        pass


    def put(self, request):

        pass


    def delete(self, request):

        pass