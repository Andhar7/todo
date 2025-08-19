from django.shortcuts import render
from todo_app.models import Todo


def home(request):
    tasks = Todo.objects.filter(completed=False).order_by('updated_at')
    context = {
        'tasks': tasks,
        'completed_tasks': Todo.objects.filter(completed=True)
    }
    print("Tasks:", tasks)
    return render(request, 'home.html', context)