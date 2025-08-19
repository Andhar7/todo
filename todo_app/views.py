# from django.http import HttpResponse
from django.shortcuts import redirect 
from .models import Todo

def addTask(request):
    task = request.POST['task']
    Todo.objects.create(title=task)
    return redirect('home')
