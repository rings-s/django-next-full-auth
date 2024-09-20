from os import getenv
from pathlib import Path
from django.core.management.utils import get_random_secret_key
# support for dotenv and getting env variables
import dotenv



# some of custom settings for deployment to digitalOcean

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



dotenv_file = BASE_DIR / '.env.local'

# load the .env file
if Path.is_file(dotenv_file):
    dotenv.load_dotenv(dotenv_file)



# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY=getenv('DJANGO_SECRET_KEY', get_random_secret_key())


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = getenv('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'users',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# video link for later aws configurations
# https://www.youtube.com/watch?v=2pZmxh8Tf78&t=3217s


# Email settings for AWS SES

# EMAIL_BACKEND = 'django_ses.SESBackend'
# DEFAULT_FROM_EMAIL = getenv('AWS_SES_DEFAULT_FROM_EMAIL')

# AWS_SES_ACCESS_KEY_ID = getenv('AWS_SES_ACCESS_KEY_ID')
# AWS_SES_SECRET_ACCESS_KEY = getenv('AWS_SES_SECRET_ACCESS_KEY')
# AWS_SES_REGION_NAME = getenv('AWS_SES_REGION_NAME')
# AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'
# AWS_SES_FROM_EMAIL = getenv('AWS_SES_FROM_EMAIL')
# USE_SES_V2 = True



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
        'users.authentication.CustomJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.UserAccount'