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
    synced_count, total_count = TodoAPIService.sync_todos()
    messages.success(request, f"Sincronizados {synced_count} nuevos TODOs de {total_count} total.")
    return redirect('todos:index')

def todos_ids_only(request):
    todos = Todo.objects.all().values('api_id')
    context = {
        'title': 'Lista de TODOs - Solo IDs',
        'todos': todos,
        'show_only': 'ids'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_ids_titles(request):
    todos = Todo.objects.all().values('api_id', 'title')
    context = {
        'title': 'Lista de TODOs - IDs y Títulos',
        'todos': todos,
        'show_only': 'ids_titles'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_pending_ids_titles(request):
    todos = Todo.objects.filter(completed=False).values('api_id', 'title')
    context = {
        'title': 'TODOs Pendientes - IDs y Títulos',
        'todos': todos,
        'show_only': 'ids_titles'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_completed_ids_titles(request):
    todos = Todo.objects.filter(completed=True).values('api_id', 'title')
    context = {
        'title': 'TODOs Completados - IDs y Títulos',
        'todos': todos,
        'show_only': 'ids_titles'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_ids_userids(request):
    todos = Todo.objects.all().values('api_id', 'user_id')
    context = {
        'title': 'Lista de TODOs - IDs y User IDs',
        'todos': todos,
        'show_only': 'ids_userids'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_completed_ids_userids(request):
    todos = Todo.objects.filter(completed=True).values('api_id', 'user_id')
    context = {
        'title': 'TODOs Completados - IDs y User IDs',
        'todos': todos,
        'show_only': 'ids_userids'
    }
    return render(request, 'todos/todo_list.html', context)

def todos_pending_ids_userids(request):
    todos = Todo.objects.filter(completed=False).values('api_id', 'user_id')
    context = {
        'title': 'TODOs Pendientes - IDs y User IDs',
        'todos': todos,
        'show_only': 'ids_userids'
    }
    return render(request, 'todos/todo_list.html', context)

def todo_list_full(request):
    todos = Todo.objects.all().order_by('-api_id')
    context = {
        'title': 'Lista Completa de TODOs',
        'todos': todos,
        'show_only': 'full'
    }
    return render(request, 'todos/todo_list.html', context)

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, api_id=todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'todos/todo_detail.html', context)

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            last_todo = Todo.objects.order_by('-api_id').first()
            todo.api_id = (last_todo.api_id + 1) if last_todo else 1
            todo.save()
            messages.success(request, 'TODO creado exitosamente.')
            return redirect('todos:todo_detail', todo_id=todo.api_id)
    else:
        form = TodoForm()
    
    context = {
        'form': form,
        'action': 'Crear'
    }
    return render(request, 'todos/todo_form.html', context)

def todo_edit(request, todo_id):
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
        'action': 'Editar',
        'todo': todo
    }
    return render(request, 'todos/todo_form.html', context)

def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, api_id=todo_id)
    
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'TODO eliminado exitosamente.')
        return redirect('todos:todo_list_full')
    
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})

@csrf_exempt
@require_http_methods(["POST"])
def todo_toggle_status(request, todo_id):
    todo = get_object_or_404(Todo, api_id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    
    return JsonResponse({
        'success': True,
        'completed': todo.completed,
        'status_text': 'Completado' if todo.completed else 'Pendiente'
    })
