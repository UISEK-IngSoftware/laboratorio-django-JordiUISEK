# Laboratorio 8. Taller Inicial de Django: Views, Templates y Modelos

Este laboratorio está diseñado para que los participantes puedan aprender y reforzar sus conocimientos de Python, HTML y CSS mediante la creación de una lista de Pokemones y una página de detalle. Utilizando como framework de desarrollo MVC a Django. De la misma manera se hará una introducción a Bootstrap para el uso de librerías de Interfaz de usuario en HTML.

Por otra parte se aplica el uso de Modelos en Django y uso de bases de datos relacionales en PostgreSQL.

## Objetivos 
- El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos (POO) como: Clases, Objetos, Atributos, Métodos. Así mismo el presente proyecto introduce al desarrollo de aplicaciones Web mediante el uso de Django como marco de trabajo para el desarrollo.
- El estudiante reforzará sus conocimientos de POO y manejo de bases de datos relacionales a través del uso de modelos en Django.

## Tareas a realizar
1. Generación de Modelos de Pokemon y Trainer.
2. Generación de migraciones.
3. Despliegue de Pokemones en Templates lista y detalle.
4. Despliegue de Entrenadores en Templates lista y detalle.

## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- PostgreSQL

### Linux
#### Instalación de gestor de ambientes virtuales de Python
```bash
sudo apt install python3-venv
```
#### Creación y activación del ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### Instalación de dependencias de este proyecto
```bash
pip3 install -r requirements.txt
```
#### Desactivación del ambiente
```bash
deactivate
```

### MacOS
#### Instalación de gestor de ambientes virtuales de Python
```bash
python3 -m venv .venv
```
#### Creación y activación del ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### Instalación de dependencias de este proyecto
```bash
pip3 install -r requirements.txt
```
#### Desactivación del ambiente
```bash
deactivate
```

### Windows
#### Instalación de gestor de ambientes virtuales de Python
```bash
pip install virtualenv
```
#### Creación del ambiente virtual
```bash
py -m venv .venv
```
#### Activación del ambiente virtual para CMD
```bash
.venv\Scripts\activate
```
#### Activación del ambiente virtual para PowerShell
```bash
.venv\Scripts\activate.ps1
```
#### Instalación de dependencias de este proyecto
```bash
pip install -r requirements.txt
```
#### Desactivación del ambiente
```bash
deactivate
```

## Comandos útiles

### Iniciar servidor
#### Linux o MacOS
```bash
python3 manage.py runserver
```
#### Windows
```bash
python manage.py runserver
```

### Crear nueva aplicación
#### Linux o MacOS
```bash
python3 manage.py startapp <nombre_de_la_aplicacion>
```
#### Windows
```bash
python manage.py startapp <nombre_de_la_aplicacion>
```

### Crear Súper Usuario
#### Linux o MacOS
```bash
python3 manage.py createsuperuser
```
#### Windows
```bash
python manage.py createsuperuser
```

### Generar archivos de migración
#### Linux o MacOS
```bash
python3 manage.py makemigrations
```
#### Windows
```bash
python manage.py makemigrations
```

### Migrar a bases de datos
#### Linux o MacOS
```bash
python3 manage.py migrate
```
#### Windows
```bash
python manage.py migrate
```

### Almacenar dependencias y librerías instaladas
#### Linux o MacOS
```bash
pip3 freeze > requirements.txt
```
#### Windows
```bash
pip freeze > requirements.txt
```

# Nota
Para los siguientes pasos se deberán seguir las instrucciones del docente en clase. No olvide que puedes contactarlo a <paperez@puce.edu.ec> o a <pablo.perez@uisek.edu.ec> dependiendo de la institución donde te encuentres.

# Ejemplos de Cadenas de Conexión para Django

### PostgreSQL
- Instalar psycopg2
    ```bash
    pip3 install psycopg2
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

### MySQL
- Instalar mysqlclient
    ```bash
    pip3 install mysqlclient
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

### SQLite
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

### Oracle
- Instalar cx_Oracle
    ```bash
    pip3 install cx_Oracle
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '1521',
        }
    }
    ```

### SQL Server (usando django-mssql-backend)
- Instalar django-mssql-backend
    ```bash
    pip3 install django-mssql-backend
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '1433',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
    ```