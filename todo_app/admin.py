from django.contrib import admin
from .models import Todo
 
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'created_at')

admin.site.register(Todo, TodoAdmin)
