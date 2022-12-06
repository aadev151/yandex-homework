from pathlib import Path

from decouple import config
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')
if config('DEBUG').lower() in ['true', 'false']:
    DEBUG = config('DEBUG').lower() == 'true'
else:
    raise ValueError(
        'DEBUG value in .env should be either \'True\' or \'False\''
    )

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split('|')

INTERNAL_IPS = [
    '127.0.0.1',
]


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
    'tinymce',
    'debug_toolbar',
    'about.apps.AboutConfig',
    'catalog.apps.CatalogConfig',
    'homepage.apps.HomepageConfig',
    'feedback.apps.FeedbackConfig',
    'users.apps.UsersConfig',
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
]

ROOT_URLCONF = 'homework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processor.getting_birthday_today',
            ],
        },
    },
]

WSGI_APPLICATION = 'homework.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev'
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


def sorl_delete(**kwargs):
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'send_mail'

SENT_FROM_EMAIL = config('SENT_FROM_EMAIL')
ADMIN_EMAIL = config('ADMIN_EMAIL')


AUTH_USER_MODEL = 'users.User'
