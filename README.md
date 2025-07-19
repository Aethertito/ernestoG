# Sistema de TODOs - Parra's Dev

Sistema web para gestión de tareas pendientes con integración a API externa y base de datos PostgreSQL.

## Características

- **7 Listas Especializadas**: Diferentes vistas de TODOs según ID, título y usuario
- **Gestión Completa**: Crear, editar, eliminar y cambiar estado de tareas
- **Sincronización API**: Integración con JSONPlaceholder para datos externos
- **Base de Datos**: PostgreSQL para almacenamiento robusto
- **Interfaz Limpia**: Diseño minimalista con navegación lateral
- **Panel Admin**: Gestión avanzada vía Django Admin

## Instalación Rápida

1. **Ejecutar configuración automática:**
   ```bash
   setup.bat
   ```

2. **Iniciar servidor:**
   ```bash
   python manage.py runserver
   ```

## URLs Principales

| Funcionalidad | URL | Descripción |
|---------------|-----|-------------|
| Dashboard | `/` | Página principal con estadísticas |
| Solo IDs | `/ids-only/` | Lista únicamente los identificadores |
| IDs + Títulos | `/ids-titles/` | Lista con IDs y títulos de tareas |
| IDs + Usuarios | `/ids-userids/` | Lista con IDs y usuarios asignados |
| Pendientes | `/pending/ids-titles/` | Tareas sin completar |
| Completados | `/completed/ids-titles/` | Tareas finalizadas |
| Lista Completa | `/list/` | Vista completa con todas las columnas |
| Crear TODO | `/create/` | Formulario para nueva tarea |
| Admin Panel | `/admin/` | Panel de administración |

## Configuración de Base de Datos

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'parradev',
        'USER': 'postgres',
        'PASSWORD': 'as12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Tecnologías

- **Backend**: Django 5.2.4
- **Base de Datos**: PostgreSQL
- **API Externa**: JSONPlaceholder
- **Frontend**: HTML5, CSS3 (sin frameworks)
- **Python**: 3.8+

## Estructura del Proyecto

```
ernestoG/
├── manage.py
├── setup.bat              # Configuración automática
├── requirements.txt       # Dependencias Python
├── todo_project/          # Configuración Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/                 # Aplicación principal
│   ├── models.py          # Modelo Todo
│   ├── views.py           # Lógica de vistas
│   ├── urls.py            # Rutas URL
│   ├── forms.py           # Formularios
│   ├── services.py        # Integración API
│   └── management/        # Comandos personalizados
└── templates/             # Plantillas HTML
    ├── base.html          # Layout principal
    └── todos/             # Templates específicos
```

## Comandos Útiles

```bash
# Sincronizar datos desde API
python manage.py sync_todos

# Verificar URLs
python manage.py test_urls

# Crear superusuario
python manage.py createsuperuser

# Limpiar base de datos
python manage.py flush
```

## Credenciales por Defecto

- **Usuario Admin**: `admin`
- **Contraseña**: `admin123`
- **Email**: `admin@parrass.dev`

## API Externa

El sistema consume datos de [JSONPlaceholder](https://jsonplaceholder.typicode.com/todos) para obtener tareas de ejemplo y mantener sincronización con datos externos.

## Soporte

Para soporte técnico o consultas:
- Email: admin@parrass.dev
- Sistema desarrollado para Parra's Dev

---

*Sistema de gestión de TODOs desarrollado con Django y PostgreSQL*
