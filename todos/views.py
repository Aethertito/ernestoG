from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Todo
from .services import TodoAPIService
from .forms import TodoForm

def index(request):
    """Vista principal con enlaces a todas las listas"""
    total_todos = Todo.objects.count()
    pending_todos = Todo.objects.filter(completed=False).count()
    completed_todos = Todo.objects.filter(completed=True).count()
    
    context = {
        'total_todos': total_todos,
        'pending_todos': pending_todos,
        'completed_todos': completed_todos,
    }
    return render(request, 'todos/index.html', context)

def sync_todos(request):
    """Sincroniza los TODOs desde la API externa"""
    synced_count, total_count = TodoAPIService.sync_todos()
    messages.success(request, f"Sincronizados {synced_count} nuevos TODOs de {total_count} total.")
    return redirect('todos:index')

# VISTAS PARA LAS LISTAS SOLICITADAS

def todos_ids_only(request):
    """Lista de todos los pendientes (solo IDs)"""
    todos = Todo.objects.all().values('api_id')
    context = {
        'title': 'Lista de TODOs - Solo IDs',
        'todos': todos,
        'show_only': 'ids'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_ids_titles(request):
    """Lista de todos los pendientes (IDs y Titles)"""
    todos = Todo.objects.all().values('api_id', 'title')
    context = {
        'title': 'Lista de TODOs - IDs y Títulos',
        'todos': todos,
        'show_only': 'ids_titles'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_pending_ids_titles(request):
    """Lista de todos los pendientes sin resolver (ID y Title)"""
    todos = Todo.objects.filter(completed=False).values('api_id', 'title')
    context = {
        'title': 'TODOs Pendientes - IDs y Títulos',
        'todos': todos,
        'show_only': 'ids_titles'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_completed_ids_titles(request):
    """Lista de todos los pendientes resueltos (ID y Title)"""
    todos = Todo.objects.filter(completed=True).values('api_id', 'title')
    context = {
        'title': 'TODOs Resueltos - IDs y Títulos',
        'todos': todos,
        'show_only': 'ids_titles'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_ids_userids(request):
    """Lista de todos los pendientes (IDs y userID)"""
    todos = Todo.objects.all().values('api_id', 'user_id')
    context = {
        'title': 'Lista de TODOs - IDs y UserIDs',
        'todos': todos,
        'show_only': 'ids_userids'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_completed_ids_userids(request):
    """Lista de todos los pendientes resueltos (ID y userID)"""
    todos = Todo.objects.filter(completed=True).values('api_id', 'user_id')
    context = {
        'title': 'TODOs Resueltos - IDs y UserIDs',
        'todos': todos,
        'show_only': 'ids_userids'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_pending_ids_userids(request):
    """Lista de todos los pendientes sin resolver (ID y userID)"""
    todos = Todo.objects.filter(completed=False).values('api_id', 'user_id')
    context = {
        'title': 'TODOs Pendientes - IDs y UserIDs',
        'todos': todos,
        'show_only': 'ids_userids'
    }
    return render(request, 'todos/todo_list.html', context)

# VISTAS CRUD

def todo_list_full(request):
    """Lista completa de TODOs con todas las columnas"""
    todos = Todo.objects.all()
    context = {
        'title': 'Lista Completa de TODOs',
        'todos': todos,
        'show_only': 'full'
    }
    return render(request, 'todos/todo_list.html', context)

def todo_detail(request, todo_id):
    """Detalle de un TODO específico"""
    todo = get_object_or_404(Todo, api_id=todo_id)
    context = {
        'todo': todo,
        'title': f'TODO #{todo.api_id}'
    }
    return render(request, 'todos/todo_detail.html', context)

def todo_create(request):
    """Crear un nuevo TODO"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'TODO creado exitosamente.')
            return redirect('todos:todo_list_full')
    else:
        form = TodoForm()
    
    context = {
        'form': form,
        'title': 'Crear Nuevo TODO',
        'action': 'Crear'
    }
    return render(request, 'todos/todo_form.html', context)

def todo_edit(request, todo_id):
    """Editar un TODO existente"""
    todo = get_object_or_404(Todo, api_id=todo_id)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'TODO actualizado exitosamente.')
            return redirect('todos:todo_detail', todo_id=todo.api_id)
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form,
        'todo': todo,
        'title': f'Editar TODO #{todo.api_id}',
        'action': 'Actualizar'
    }
    return render(request, 'todos/todo_form.html', context)

def todo_delete(request, todo_id):
    """Eliminar un TODO"""
    todo = get_object_or_404(Todo, api_id=todo_id)
    
    if request.method == 'POST':
        todo.delete()
        messages.success(request, f'TODO #{todo_id} eliminado exitosamente.')
        return redirect('todos:todo_list_full')
    
    context = {
        'todo': todo,
        'title': f'Eliminar TODO #{todo.api_id}'
    }
    return render(request, 'todos/todo_confirm_delete.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def todo_toggle_status(request, todo_id):
    """Cambiar el estado de completado de un TODO vía AJAX"""
    todo = get_object_or_404(Todo, api_id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    
    return JsonResponse({
        'success': True,
        'completed': todo.completed,
        'status_display': todo.status_display
    })
