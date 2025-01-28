from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'date_create')  # Поля, которые будут отображаться в списке
    search_fields = ('task',)  # Поля, по которым можно будет искать
    
admin.site.register(ToDo)