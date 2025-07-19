@echo off
title Sistema de TODOs - Configuracion Automatica
color 0A
echo.
echo ========================================
echo     SISTEMA DE TODOs - PARRA'S DEV
echo     Configuracion Automatica v1.0
echo ========================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor instale Python 3.8+ desde python.org
    pause
    exit /b 1
)

REM Verificar si PostgreSQL esta corriendo
echo [INFO] Verificando PostgreSQL...
psql -U postgres -d parradev -c "SELECT 1;" >nul 2>&1
if errorlevel 1 (
    echo ADVERTENCIA: No se puede conectar a PostgreSQL
    echo Asegurese de que PostgreSQL este corriendo y la BD 'parradev' exista
    echo.
)

REM Cambiar al directorio del proyecto
cd /d "%~dp0"

echo [1/7] Instalando dependencias de Python...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo     ✓ Dependencias instaladas correctamente

echo.
echo [2/7] Realizando migraciones de base de datos...
python manage.py makemigrations
if errorlevel 1 (
    echo ERROR: Error al crear migraciones
    pause
    exit /b 1
)

python manage.py migrate
if errorlevel 1 (
    echo ERROR: Error al aplicar migraciones
    pause
    exit /b 1
)
echo     ✓ Base de datos configurada correctamente

echo.
echo [3/7] Creando superusuario admin...
echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@parrass.dev', 'admin123') if not User.objects.filter(username='admin').exists() else print('Usuario admin ya existe') | python manage.py shell
echo     ✓ Superusuario configurado

echo.
echo [4/7] Sincronizando datos desde JSONPlaceholder API...
python manage.py sync_todos
if errorlevel 1 (
    echo ADVERTENCIA: Error al sincronizar TODOs desde API
) else (
    echo     ✓ Datos sincronizados desde API externa
)

echo.
echo [5/7] Verificando URLs del sistema...
python manage.py test_urls
if errorlevel 1 (
    echo ADVERTENCIA: Algunas URLs pueden tener problemas
) else (
    echo     ✓ Todas las URLs funcionan correctamente
)

echo.
echo [6/7] Verificando conexion a base de datos...
python manage.py check --database default
if errorlevel 1 (
    echo ADVERTENCIA: Problemas con la base de datos
) else (
    echo     ✓ Conexion a PostgreSQL establecida
)

echo.
echo [7/7] Creando archivos de inicio rapido...

REM Crear script de inicio rapido
echo @echo off > start_server.bat
echo title TODO System - Servidor de Desarrollo >> start_server.bat
echo echo Iniciando servidor en http://127.0.0.1:8000/ >> start_server.bat
echo python manage.py runserver >> start_server.bat
echo pause >> start_server.bat

echo     ✓ Archivo start_server.bat creado

echo.
echo ========================================
echo     CONFIGURACION COMPLETADA!
echo ========================================
echo.
echo CREDENCIALES DEL SISTEMA:
echo ------------------------
echo Usuario Admin: admin
echo Contraseña: admin123
echo Email: admin@parrass.dev
echo.
echo BASE DE DATOS:
echo --------------
echo Host: localhost
echo Base de Datos: parradev
echo Usuario: postgres
echo Contraseña: as12345
echo.
echo URLS PRINCIPALES:
echo ----------------
echo Dashboard: http://127.0.0.1:8000/
echo Panel Admin: http://127.0.0.1:8000/admin/
echo Sincronizar API: http://127.0.0.1:8000/sync/
echo.
echo LISTAS DISPONIBLES:
echo ------------------
echo Solo IDs: http://127.0.0.1:8000/ids-only/
echo IDs + Titulos: http://127.0.0.1:8000/ids-titles/
echo IDs + Usuarios: http://127.0.0.1:8000/ids-userids/
echo Pendientes: http://127.0.0.1:8000/pending/ids-titles/
echo Completados: http://127.0.0.1:8000/completed/ids-titles/
echo.
echo ARCHIVOS CREADOS:
echo ----------------
echo - start_server.bat (para iniciar el servidor)
echo.
echo ========================================
echo Para iniciar el servidor ahora ejecute:
echo python manage.py runserver
echo.
echo O use el archivo: start_server.bat
echo ========================================
echo.
pause
