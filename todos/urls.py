from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    
    # Sincronización con API
    path('sync/', views.sync_todos, name='sync'),
    
    # LISTAS SOLICITADAS EN EL EXAMEN
    # Lista de todos los pendientes (solo IDs)
    path('ids-only/', views.todos_ids_only, name='todos_ids_only'),
    
    # Lista de todos los pendientes (IDs y Titles)
    path('ids-titles/', views.todos_ids_titles, name='todos_ids_titles'),
    
    # Lista de todos los pendientes sin resolver (ID y Title)
    path('pending/ids-titles/', views.todos_pending_ids_titles, name='todos_pending_ids_titles'),
    
    # Lista de todos los pendientes resueltos (ID y Title)
    path('completed/ids-titles/', views.todos_completed_ids_titles, name='todos_completed_ids_titles'),
    
    # Lista de todos los pendientes (IDs y userID)
    path('ids-userids/', views.todos_ids_userids, name='todos_ids_userids'),
    
    # Lista de todos los pendientes resueltos (ID y userID)
    path('completed/ids-userids/', views.todos_completed_ids_userids, name='todos_completed_ids_userids'),
    
    # Lista de todos los pendientes sin resolver (ID y userID)
    path('pending/ids-userids/', views.todos_pending_ids_userids, name='todos_pending_ids_userids'),
    
    # CRUD COMPLETO
    path('list/', views.todo_list_full, name='todo_list_full'),
    path('detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    
    # AJAX para cambio de estado
    path('toggle/<int:todo_id>/', views.todo_toggle_status, name='todo_toggle_status'),
]
