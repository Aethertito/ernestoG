from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['api_id', 'title', 'user_id', 'completed', 'created_at']
    list_filter = ['completed', 'user_id', 'created_at']
    search_fields = ['title', 'api_id']
    list_editable = ['completed']
    ordering = ['api_id']
    
    fieldsets = (
        ('Información de la API', {
            'fields': ('api_id', 'user_id')
        }),
        ('Contenido', {
            'fields': ('title', 'completed')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
