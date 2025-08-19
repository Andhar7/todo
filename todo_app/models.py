from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Todo Item'
        verbose_name_plural = 'Todo Items'

# The Meta class in Django models is a special class that contains metadata about the model. In this specific Todo model, the Meta class defines three important configurations:

# ordering = ['-created_at']

# This sets the default ordering of Todo items
# The - prefix means descending order
# Todo items will be sorted by creation date with newest items first

# verbose_name = 'Todo Item'

# This sets a human-readable singular name for the model
# Used in the Django admin interface and other places where the model name is displayed
# Instead of showing "Todo", it will display as "Todo Item"

# verbose_name_plural = 'Todo Items'

# Sets the plural name for the model
# Without this, Django would automatically add 's' to the singular name
# Now it will show "Todo Items" instead of "Todos"
# The Meta class can include many other options like:

# db_table - to specify custom database table name
# indexes - to define database indexes
# permissions - to add custom permissions
# abstract - to mark the model as abstract base class