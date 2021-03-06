import os
from pathlib import Path
from celery.schedules import crontab
from django.urls import reverse_lazy
# from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# load_dotenv(BASE_DIR / ".." / ".env.example")  # take environment variables from .env.example

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+cjh*h^-%in2sxg*i%48(y1&bzhc9ox4d31$b@of&&l5da1@u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('ENV') == 'dev'

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'books',
    'accounts',

    'django_extensions',
    'debug_toolbar',
    'crispy_forms',

    'rest_framework',
    'drf_yasg',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'booksharing.middlewares.SimpleMiddleware',
]

ROOT_URLCONF = 'booksharing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'books.context_processor.model_choices_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'booksharing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = '/tmp/static'
MEDIA_ROOT = BASE_DIR / '..' / 'media'
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_BROKER_URL = 'amqp://{0}:{1}@{2}:{3}//'.format(
    os.environ['RABBITMQ_DEFAULT_USER'],
    os.environ['RABBITMQ_DEFAULT_PASS'],
    os.environ.get('RABBITMQ_DEFAULT_HOST', '127.0.0.1'),
    os.environ.get('RABBITMQ_DEFAULT_PORT', '5672'),
)


CELERY_BEAT_SCHEDULE = {
    'debug': {
        'task': 'accounts.tasks.debug',
        'schedule': crontab(minute='*/1'),
    },
}


LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGOUT_REDIRECT_URL = reverse_lazy("index")

AUTH_USER_MODEL = "accounts.User"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{}:{}'.format(
            os.environ.get('CACHE_HOST', '127.0.0.1'),
            os.environ.get('CACHE_PORT', '11211'),
        ),
        # 'LOCATION': 'my-domain.com:11211',
    }
}


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

if DEBUG:
    import socket

    ALLOWED_HOSTS = ['*']

    # debug tool_bar
    DEBUG_TOOLBAR_PATCH_SETTINGS = True
    INTERNAL_IPS = ['127.0.0.1']

    # tricks to have debug toolbar when developing with docker
    ip = socket.gethostbyname(socket.gethostname())
    ip = '.'.join(ip.split('.')[:-1])
    ip = f'{ip}.1'
    INTERNAL_IPS.append(ip)
