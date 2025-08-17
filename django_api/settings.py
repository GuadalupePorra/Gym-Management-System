
import os
from pathlib import Path

import dj_database_url

AUTH_USER_MODEL = 'usuario_sistema.UsuarioSistema' 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m(o$-ldz!0wp$zbe&s3d(goh&kr(lwknvir!m#!fxokvhm6@o)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'zeus-gym-production.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'jazzmin', 
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'clases',
    'membresias',
    'usuario_sistema',
    'socios',
    'caja',
    'ingreso_diario',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CELERY_BROKER_URL = 'redis://localhost:6379/0'
 

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
]
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS"
]

ROOT_URLCONF = 'django_api.urls'

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",                # tus templates normales
            BASE_DIR / "gym-frontend" / "build",  # build de React
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_api.wsgi.application'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:NnJVQltzQLzKSVIAlEYDGgVdmzfKYEcG@postgres.railway.internal:5432/railway',
        conn_max_age=600
    )

}""" 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'NnJVQltzQLzKSVIAlEYDGgVdmzfKYEcG',
        'HOST': 'crossover.proxy.rlwy.net',
        'PORT': '33074',
    }

}




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
   
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]




LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'  

USE_I18N = True # Permite traducir textos y adaptarse a diferentes idiomas

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'caja', 'static'),
    os.path.join(BASE_DIR, 'gym-frontend', 'build','static'),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "login_logo": "/img/logo.png",
    "custom_css": "css/jazz.css",
    "site_title": "Zeus Gym",
    "site_header": "Zeus Gym",
    "site_brand": "Zeus Gym",
    "welcome_sign": "Bienvenido/a al sistema de gestión",

    "show_ui_builder": True,
    
    "icons": {
        "ingreso_diario.Ingreso_diario": "fas fa-calendar-check",        # Ingresos registrados
        "socios.Socio": "fas fa-user",                                   # Socios registrados
        "clases.Clase": "fas fa-dumbbell",                               # Clases registradas
        "clases.Horario_Clases": "fas fa-clock",                         # Horarios registrados
        "caja.Pago": "fas fa-cash-register",                             # Pagos registrados
        "membresias.Membresia": "fas fa-id-card-alt",                    # Membresías registradas
        "usuario_sistema.UsuarioSistema": "fas fa-users-cog",        
    },
    "model_icons": {
        "socios.socio": "fas fa-users",  # redundante pero seguro
    },
    "order_with_respect_to": ["socios", "socios.socio"],
    

    "side_menu": [
        {
            "app": "socios",
            "label": "Gestión de Socios",
            "icon": "fas fa-users",
            "models": [
                {
                    "name": "socios.socio",               # app.model
                    "label": "Socios registrados",         # <- texto que ves en el panel
                    "icon": "fas fa-id-badge",             # <- ícono de la lista
                    "permissions": ["socios.view_socio"]
                },
            ],
           
        }
    ],

    "hide_apps": [
        "auth",
    ],
    
    
    'topmenu_links': [
        {"name": "Registrar ingreso diario de un socio", "url": "/admin/ingreso_diario/ingreso_diario/add/", "permissions": []},
        {"name": "Ver Socios", "url": "/admin/socios/socio/", "permissions": []},
        {"name": "Ver Clases", "url": "/admin/clases/clase/", "permissions": []},
        {"name": "Registrar pago", "url": "/admin/caja/pago/add/", "permissions": []},
    ],

    "order_with_respect_to": ["ingreso_diario", "socios", "clases", "caja"],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-warning",
    "accent": "accent-navy",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "flatly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-success",
        "secondary": "btn-secondary",
        "info": "btn-dark",
        "warning": "btn-outline-warning",
        "danger": "btn-danger",
        "success": "btn-warning"
    },
    "actions_sticky_top": True
}
