# ⚡ Parra's Dev - Pizarra de Pendientes

## Descripción del Proyecto

Aplicación web Django moderna desarrollada para **Parra's Dev** que resuelve el problema de la pizarra de pendientes (ToDo). La aplicación consume datos de una API externa y proporciona todas las funcionalidades CRUD necesarias para gestionar los pendientes con un diseño minimalista y único.

## 🎯 Características Principales

### Listas Solicitadas (Según Especificaciones)
1. **Lista de todos los pendientes (solo IDs)**
2. **Lista de todos los pendientes (IDs y Titles)**
3. **Lista de todos los pendientes sin resolver (ID y Title)**
4. **Lista de todos los pendientes resueltos (ID y Title)**
5. **Lista de todos los pendientes (IDs y userID)**
6. **Lista de todos los pendientes resueltos (ID y userID)**
7. **Lista de todos los pendientes sin resolver (ID y userID)**

### Funcionalidades CRUD Completas
- ✅ **CREATE**: Crear nuevos TODOs
- 👁️ **READ**: Ver listas y detalles de TODOs
- ✏️ **UPDATE**: Editar TODOs existentes
- 🗑️ **DELETE**: Eliminar TODOs

### Características Adicionales
- 🔄 **Sincronización con API externa** (JSONPlaceholder)
- 📊 **Dashboard con estadísticas en tiempo real**
- 🎨 **Diseño minimalista único** (no genérico)
- ⚡ **Cambio de estado vía AJAX**
- 👑 **Panel de administración Django**
- 📱 **Responsive design**

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Aplicar migraciones**:
   ```bash
   python manage.py migrate
   ```

3. **Crear superusuario** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

4. **Sincronizar datos desde la API**:
   ```bash
   python manage.py sync_todos
   ```

5. **Ejecutar servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación**:
   - Aplicación principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
ernestoG/
├── todo_project/          # Configuración principal del proyecto Django
│   ├── settings.py        # Configuraciones
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuración WSGI
├── todos/                # Aplicación principal de TODOs
│   ├── models.py         # Modelo Todo
│   ├── views.py          # Vistas para todas las funcionalidades
│   ├── urls.py           # URLs de la aplicación
│   ├── forms.py          # Formularios para CRUD
│   ├── services.py       # Servicio para consumir API
│   ├── admin.py          # Configuración del admin
│   └── management/       # Comandos personalizados
│       └── commands/
│           └── sync_todos.py
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base con diseño "feo"
│   └── todos/            # Plantillas específicas
├── static/               # Archivos estáticos
├── manage.py             # Comando principal de Django
└── requirements.txt      # Dependencias del proyecto
```

## 🌐 URLs Disponibles

### Página Principal
- `/` - Página principal con menú de navegación

### Listas Solicitadas
- `/ids-only/` - Solo IDs
- `/ids-titles/` - IDs y Títulos (todos)
- `/pending/ids-titles/` - IDs y Títulos (pendientes)
- `/completed/ids-titles/` - IDs y Títulos (resueltos)
- `/ids-userids/` - IDs y UserIDs (todos)
- `/pending/ids-userids/` - IDs y UserIDs (pendientes)
- `/completed/ids-userids/` - IDs y UserIDs (resueltos)

### CRUD Completo
- `/list/` - Lista completa con todas las columnas
- `/create/` - Crear nuevo TODO
- `/detail/<id>/` - Ver detalle de TODO
- `/edit/<id>/` - Editar TODO
- `/delete/<id>/` - Eliminar TODO

### Utilidades
- `/sync/` - Sincronizar con API externa
- `/admin/` - Panel de administración Django

## 🔧 Comandos de Administración

### Sincronizar TODOs desde API
```bash
python manage.py sync_todos
```

### Sincronización forzada
```bash
python manage.py sync_todos --force
```

## 🎨 Diseño Minimalista Único

El diseño de la aplicación es limpio, moderno y distintivo:

- ✅ **Paleta de colores personalizada**: Azules, grises y acentos dorados
- ✅ **Tipografía moderna**: SF Pro Display/Inter con fallbacks del sistema
- ✅ **Gradientes sutiles**: Fondos con degradados suaves
- ✅ **Componentes con bordes redondeados**: 12-16px de radio
- ✅ **Sombras suaves**: Efectos de profundidad elegantes
- ✅ **Animaciones fluidas**: Transiciones CSS suaves
- ✅ **Layout responsive**: Adaptable a dispositivos móviles
- ✅ **Micro-interacciones**: Hover effects y estados visuales

## 🔌 API Externa

La aplicación consume datos de **JSONPlaceholder**:
- URL: https://jsonplaceholder.typicode.com/todos
- Proporciona 200 TODOs de prueba
- Estructura: { id, userId, title, completed }

## 🧪 Datos de Prueba

Después de ejecutar la sincronización:
- **200 TODOs** totales
- **100 TODOs** completados
- **100 TODOs** pendientes
- **10 usuarios** diferentes (userIds 1-10)

## 👥 Usuarios de Prueba

### Superusuario Admin
- **Usuario**: admin
- **Contraseña**: admin123
- **Email**: admin@parrass.dev

## 🚀 Despliegue en Producción

Para despliegue en producción (ej. Heroku):

1. **Configurar variables de entorno**
2. **Usar base de datos PostgreSQL**
3. **Configurar archivos estáticos**
4. **Usar Gunicorn como servidor WSGI**

El archivo `Procfile` ya está incluido para Heroku.

## 📞 Soporte

Para cualquier duda o problema:
- Desarrollado por: **Parra's Dev Team**
- Fecha: Julio 2025
- Tecnologías: Python, Django, HTML, CSS, JavaScript

---

## ⚠️ Nota sobre el Diseño

Este proyecto presenta un diseño minimalista único que no es genérico. Utiliza una paleta de colores cuidadosamente seleccionada, componentes modernos con bordes redondeados, gradientes sutiles y micro-interacciones que hacen que la experiencia de usuario sea agradable sin ser común. La funcionalidad es completamente robusta y cumple con los estándares de calidad de código de Parra's Dev.

**¡La información oportuna y confiable permite tomar las mejores decisiones!** 🎯
