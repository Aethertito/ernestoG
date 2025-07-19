from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('sync/', views.sync_todos, name='sync'),
    
    path('ids-only/', views.todos_ids_only, name='todos_ids_only'),
    
    path('ids-titles/', views.todos_ids_titles, name='todos_ids_titles'),
    
    path('pending/ids-titles/', views.todos_pending_ids_titles, name='todos_pending_ids_titles'),
    
    path('completed/ids-titles/', views.todos_completed_ids_titles, name='todos_completed_ids_titles'),
    
    path('ids-userids/', views.todos_ids_userids, name='todos_ids_userids'),
    
    path('completed/ids-userids/', views.todos_completed_ids_userids, name='todos_completed_ids_userids'),
    
    path('pending/ids-userids/', views.todos_pending_ids_userids, name='todos_pending_ids_userids'),
    
    path('list/', views.todo_list_full, name='todo_list_full'),
    path('detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    
    path('toggle/<int:todo_id>/', views.todo_toggle_status, name='todo_toggle_status'),
]
