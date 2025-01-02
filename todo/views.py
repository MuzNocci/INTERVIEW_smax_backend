from django.shortcuts import render
from django.views import View



class HomeView(View):

    def get(request):

        context = {
            'title':'To do list'
        }
        return render(request, 'page.html', context)