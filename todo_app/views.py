# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect 
from .models import Todo

def addTask(request):
    task = request.POST['task']
    Todo.objects.create(title=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.completed = True
    task.save()
    return redirect('home')
