# INFORMACIÓN RÁPIDA - Sistema de TODOs

## CONFIGURACIÓN INICIAL
1. Ejecutar: `setup.bat`
2. Iniciar servidor: `start_server.bat` o `python manage.py runserver`

## ACCESOS RÁPIDOS
- **Dashboard**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Usuario**: admin / admin123

## LISTAS PRINCIPALES
- `/ids-only/` - Solo identificadores
- `/ids-titles/` - IDs y títulos  
- `/ids-userids/` - IDs y usuarios
- `/pending/ids-titles/` - Pendientes
- `/completed/ids-titles/` - Completados

## BASE DE DATOS
- **Host**: localhost
- **BD**: parradev
- **Usuario**: postgres  
- **Contraseña**: as12345

## COMANDOS ÚTILES
```bash
python manage.py sync_todos     # Sincronizar API
python manage.py test_urls      # Verificar URLs
python manage.py createsuperuser # Crear admin
```

## ARCHIVOS IMPORTANTES
- `setup.bat` - Configuración automática completa
- `start_server.bat` - Inicio rápido del servidor
- `manage.py` - Comandos Django
- `requirements.txt` - Dependencias Python
