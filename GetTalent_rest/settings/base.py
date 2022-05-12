from pathlib import Path
import os
from re import TEMPLATE


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^9%(8f)mecpbj-4p123vua1ze3nqhr@q^+kvdt0-%n4%k1g*#x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
#Aplicaciones base que vienen por defecto 
BASE_APPS = [
    'django.contrib.admin',  #Se comenta cuando se borran las migreaciones para correr desde cero
    'django.contrib.auth',   #
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#Aplicaciones locales, las que yo estoy creando
LOCAL_APPS = [
    'apps.users',   #GT Enlazar esta base de users con la otra aplicación
    
]
#Aplicaciones de terceros, las librerias externas que ocuparé en algun momento
THIRD_APPS =[
    'rest_framework',
    # 'rest_framework.authtoken',   
    # 'rest_auth',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'rest_auth.registration',
    'simple_history',    
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

# AUTH_USER_MODEL = 'users.User'   #GT Mi aplicación va a funcionar con un modelo llamada usuario
AUTH_USER_MODEL = 'users.CustomUser' #GT segundo ejercicio

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware'   #GT poblar de manera automatica la base de datos para usuarios
]

ROOT_URLCONF = 'GetTalent_rest.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS':[],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))
# # Find templates in the same folder as settings.py.

# TEMPLATE_DIRS = (
#     '/home/scharahzada/Documentos/PROYECTO_BOOTCAMP/GET_TALENT/Prueba2/GetTalent_rest/GetTalent_rest/templates'
#     os.path.join(SETTINGS_PATH, 'templates'),
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':['GetTalent_rest/templates',],                                                   #[os.path.join(BASE_DIR,'templates')],  #GT se edita para proyecto
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


#Inicio y cierre de sesión
LOGIN_REDIRECT_URL = 'home'   #Asi esta configurado en GetTalent_rest/urls.py     #"/" 
LOGOUT_REDIRECT_URL = 'home'  #Asi esta configurado en GetTalent_rest/urls.py  # "/"

WSGI_APPLICATION = 'GetTalent_rest.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DJANGO-ALLAUTH CONFIGURACIÓN

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'    #GT Uso de correo electrónico en lugar de nombre de usuario
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'   #GT Enviar el mensaje de verificación de correo electrónico al registrarse el usuario con el enlace de verificación
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'   #GT Cuando el usuario hace clic en el enlace, su correo electrónico se verifica y se redirige a/?verification=1
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'   #GT cuando el usuario hace clic en el enlace, su correo electrónico se verifica y se redirige a/?verification=1

# SITE_ID = 1
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Serializador

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
}

# SMTP Server
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"













