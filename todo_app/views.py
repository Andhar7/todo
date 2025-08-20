# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render 
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

def mark_as_not_done(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        task.title = request.POST['task']
        task.description = request.POST.get('description', '')
        task.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task': task})
