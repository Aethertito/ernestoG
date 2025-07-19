import requests
from django.conf import settings
from .models import Todo

class TodoAPIService:
    """
    Servicio para manejar la comunicación con la API externa de TODOs
    """
    BASE_URL = "https://jsonplaceholder.typicode.com/todos"
    
    @classmethod
    def fetch_todos_from_api(cls):
        """
        Obtiene todos los TODOs de la API externa
        """
        try:
            response = requests.get(cls.BASE_URL, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener TODOs de la API: {e}")
            return []
    
    @classmethod
    def sync_todos(cls):
        """
        Sincroniza los TODOs de la API con la base de datos local
        """
        api_todos = cls.fetch_todos_from_api()
        synced_count = 0
        
        for api_todo in api_todos:
            todo, created = Todo.objects.update_or_create(
                api_id=api_todo['id'],
                defaults={
                    'user_id': api_todo['userId'],
                    'title': api_todo['title'],
                    'completed': api_todo['completed']
                }
            )
            if created:
                synced_count += 1
        
        return synced_count, len(api_todos)
    
    @classmethod
    def get_todo_by_id(cls, todo_id):
        """
        Obtiene un TODO específico por ID de la API
        """
        try:
            response = requests.get(f"{cls.BASE_URL}/{todo_id}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener TODO {todo_id}: {e}")
            return None
