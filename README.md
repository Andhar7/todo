
```zsh
# Create virtual environment
python3 -m venv ckg
source ckg/bin/activate

# Install Django
pip install django

# Create django project
django-admin startproject todo_main

# Create django app
django-admin startapp todo_app

# Cteate models
# Add 'todo_app' to INSTALLED_APPS in todo_main/settings.py
# Define models in todo_app/models.py   


# Create migrations 
python3 manage.py makemigrations       
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser
# Run server
python3 manage.py runserver

# Go to todo_main/views.py and create logic for the home page


# With React/Vite, you can use PUT method since you'll be making AJAX requests instead of HTML form submissions. Let me show you how the backend would look to handle PUT requests:

#  Modified Backend for PUT Requests:
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import Todo

# Option 1: Function-based view with PUT support
@csrf_exempt  # You'd handle CSRF differently in production
@require_http_methods(["GET", "PUT"])
def edit_task_api(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'GET':
        # Return task data as JSON
        return JsonResponse({
            'id': task.pk,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'created_at': task.created_at.isoformat(),
            'updated_at': task.updated_at.isoformat()
        })
    
    elif request.method == 'PUT':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            
            # Update task fields
            title = data.get('title', '').strip()
            description = data.get('description', '').strip()
            
            if not title:
                return JsonResponse({
                    'error': 'Title is required'
                }, status=400)
            
            task.title = title
            task.description = description
            task.save()
            
            # Return updated task data
            return JsonResponse({
                'id': task.pk,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat(),
                'updated_at': task.updated_at.isoformat(),
                'message': 'Task updated successfully'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=500)

# Option 2: Class-based view (more RESTful)
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class TaskAPIView(View):
    def get(self, request, pk):
        task = get_object_or_404(Todo, pk=pk)
        return JsonResponse({
            'id': task.pk,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'created_at': task.created_at.isoformat(),
            'updated_at': task.updated_at.isoformat()
        })
    
    def put(self, request, pk):
        task = get_object_or_404(Todo, pk=pk)
        
        try:
            data = json.loads(request.body)
            
            title = data.get('title', '').strip()
            description = data.get('description', '').strip()
            
            if not title:
                return JsonResponse({'error': 'Title is required'}, status=400)
            
            task.title = title
            task.description = description
            task.save()
            
            return JsonResponse({
                'id': task.pk,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat(),
                'updated_at': task.updated_at.isoformat(),
                'message': 'Task updated successfully'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


# 🛣️ Updated URLs:
# In todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Existing HTML form routes
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    
    # New API routes for React
    path('api/task/<int:pk>/', views.edit_task_api, name='edit_task_api'),
    # OR using class-based view
    path('api/task/<int:pk>/', views.TaskAPIView.as_view(), name='task_api'),
]

# ⚛️ React/Vite Frontend Example:
// React component example
const EditTask = ({ taskId }) => {
  const [task, setTask] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  // Fetch task data
  useEffect(() => {
    fetch(`/todo/api/task/${taskId}/`)
      .then(response => response.json())
      .then(data => {
        setTask(data);
        setTitle(data.title);
        setDescription(data.description);
      });
  }, [taskId]);

  // Handle PUT request
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch(`/todo/api/task/${taskId}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'), // CSRF handling
        },
        body: JSON.stringify({
          title,
          description
        })
      });

      if (response.ok) {
        const updatedTask = await response.json();
        console.log('Task updated:', updatedTask);
        // Handle success (redirect, show message, etc.)
      } else {
        const error = await response.json();
        console.error('Error:', error);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button type="submit">Update Task</button>
    </form>
  );
};


# 🚀 With Django REST Framework (Recommended):
# For a production React app, I'd recommend using Django REST Framework:
# Using DRF (cleaner approach)
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
# Automatically handles GET, POST, PUT, PATCH, DELETE