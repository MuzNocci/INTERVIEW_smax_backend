from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from todo.models import Task



class ToDoListAndAdd(View):


    def get(self, request):

        tasks = Task.objects.all()[::-1]

        context = {
            'title':'ToDo | Sistema de Lista de Tarefas',
            'tasks': tasks,
        }
        return render(request, 'todo.view.html', context)
    

    def post(self, request):

        new_task = Task(task=request.POST.get("task"))

        try:
            new_task.save()
            return redirect('list')
        
        except:
            return redirect('list')


class ToDoEdit(View):


    def get(self, request, id):

        task = get_object_or_404(Task, id=id)

        context = {
            'title':'ToDo | Edite a tarefa',
            'task': task,
        }
        return render(request, 'todo.edit.html', context)


    def post(self, request, id):

        task = get_object_or_404(Task, id=id)
        task.task = request.POST.get("task")
        task.save()

        return redirect('list')


class ToDoDelete(View):


    def get(self, request, id):

        task = get_object_or_404(Task, id=id)

        context = {
            'title':'ToDo | Delete a tarefa',
            'task': task,
        }
        return render(request, 'todo.delete.html', context)


    def post(self, request, id):

        task = get_object_or_404(Task, id=id)
        task.delete()

        return redirect('list')