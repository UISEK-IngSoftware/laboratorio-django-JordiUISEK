![Pokedex](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7wZrdn7upNp8rQQaLJU_2dw-irIDQeNsnIQ&s)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![OAuth2](https://img.shields.io/badge/OAuth2-000000?style=for-the-badge&logo=oauth&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

# Laboratorio 8: Aplicación Pokedex con Django

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Django que simula una Pokedex digital. Permite gestionar información de Pokemon y Entrenadores, incluyendo funcionalidades CRUD completas, API REST, autenticación OAuth2 y una interfaz web moderna con Bootstrap.

## Características Principales

- **Gestión de Pokemon**: Crear, leer, actualizar y eliminar información de Pokemon
- **Gestión de Entrenadores**: Administrar datos de entrenadores Pokemon
- **API REST**: Endpoints completos para Pokemon y Entrenadores
- **Autenticación OAuth2**: Sistema de autenticación seguro
- **Interfaz Web**: Templates HTML con Bootstrap para una experiencia de usuario moderna
- **Base de Datos SQLite**: Almacenamiento local y portable
- **Procesamiento de Imágenes**: Carga y gestión de imágenes de Pokemon y Entrenadores
- **CORS Configurado**: Permite comunicación entre diferentes dominios

## Estructura del Proyecto

```
laboratorio-django-JordiUISEK/
├── api/                    # Aplicación para API REST
│   ├── serializers.py     # Serializers para Pokemon y Trainer
│   ├── views.py          # Vistas de la API
│   └── urls.py           # URLs de la API
├── lab8/                  # Configuración principal del proyecto
│   ├── settings.py       # Configuración de Django
│   └── urls.py          # URLs principales
├── pokedex/              # Aplicación principal
│   ├── models.py        # Modelos Pokemon y Trainer
│   ├── views.py         # Vistas web
│   ├── templates/       # Templates HTML
│   └── static/          # Archivos estáticos (CSS, JS, imágenes)
├── media/               # Archivos multimedia subidos
│   ├── pokemon_images/  # Imágenes de Pokemon
│   └── trainer_images/  # Imágenes de Entrenadores
└── requirements.txt     # Dependencias del proyecto
```

## Modelos de Datos

### Pokemon
- **name**: Nombre del Pokemon (CharField, max_length=40)
- **type**: Tipo del Pokemon (CharField, max_length=30)
- **weight**: Peso del Pokemon (IntegerField)
- **height**: Altura del Pokemon (IntegerField)
- **description**: Descripción opcional (CharField, max_length=150)
- **picture**: Imagen del Pokemon (ImageField)

### Trainer
- **name**: Nombre del Entrenador (CharField, max_length=40)
- **age**: Edad del Entrenador (IntegerField)
- **weight**: Peso del Entrenador (IntegerField)
- **height**: Altura del Entrenador (IntegerField)
- **catch**: Número de Pokemon capturados (IntegerField)
- **description**: Descripción opcional (CharField, max_length=150)
- **picture**: Imagen del Entrenador (ImageField)

## Tecnologías Utilizadas

- **Backend**: Django 5.2.4
- **Lenguaje**: Python 3.10+
- **Base de Datos**: SQLite (incluido con Python)
- **API**: Django REST Framework 3.16.0
- **Autenticación**: OAuth2 con django-oauth-toolkit
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.6
- **Procesamiento de Imágenes**: Pillow 11.2.1
- **CORS**: django-cors-headers 4.7.0

## Instalación y Configuración

### Requisitos Previos

- Python 3.10 o superior
- Git

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd laboratorio-django-JordiUISEK
   ```

2. **Crear ambiente virtual**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/MacOS
   # o
   .venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   Crear un archivo `.env` en la raíz del proyecto:
   ```
   SECRET_KEY=tu-clave-secreta-aqui
   DEBUG=True
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar servidor**
   ```bash
   python manage.py runserver
   ```

## Uso de la Aplicación

### Interfaz Web
- Acceder a `http://localhost:8000` para la interfaz principal
- Navegar a `/admin` para el panel de administración
- Usar los formularios para crear y editar Pokemon y Entrenadores

### API REST
- **Pokemon**: `/api/pokemon/`
- **Entrenadores**: `/api/trainer/`
- **Autenticación**: OAuth2 endpoints disponibles

### Comandos Útiles

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear nueva aplicación
python manage.py startapp nombre_app

# Crear superusuario
python manage.py createsuperuser

# Generar migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar tests
python manage.py test

# Recolectar archivos estáticos
python manage.py collectstatic
```

## Configuración de Base de Datos

### SQLite (Configuración por defecto)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Variables de Entorno
Crear archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Configuración de Media Files
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Configuración de Static Files
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

## Usuario de acceso
- **Usuario:** jordi
- **Contraseña:** jordi

## Deployment

### Configuración para Producción
1. Cambiar `DEBUG = False`
2. Configurar `ALLOWED_HOSTS`
3. Configurar base de datos de producción
4. Configurar variables de entorno
5. Ejecutar `python manage.py collectstatic`
6. Configurar servidor web (Nginx, Apache)

### Docker (Opcional)
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Troubleshooting

### Problemas Comunes

1. **Error de migraciones**
   ```bash
   python manage.py makemigrations --empty pokedex
   python manage.py migrate
   ```

2. **Error de permisos de archivos**
   ```bash
   chmod -R 755 media/
   ```

3. **Error de conexión a base de datos**
   - Verificar que el archivo db.sqlite3 existe
   - Verificar permisos de escritura en el directorio
   - Ejecutar migraciones si es necesario

4. **Error de CORS**
   - Verificar configuración en settings.py
   - Verificar origen de las peticiones

## Laboratorio 9: Frontend

Repositorio GIT API REST: https://github.com/UISEK-IngSoftware/laboratorio-9-JordiUISEK
```
git clone git@github.com:UISEK-IngSoftware/laboratorio-9-JordiUISEK.git
```

Ejecutar el servidor
```
npm run dev
```