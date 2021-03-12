"""
Django settings for mysait project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$@3eo644i5w$4(akk&k&l(=^c!i(rk1($)c0&!!y1zey1rp0o6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'send_email',

    # 'accounts',
    # 'social_django'
]


'''AUTHENTICATION_BACKENDS = (
    # бекенд авторизации через ВКонтакте
    # 'django.contrib.auth.backends.ModelBackend',
    # 'social_core.backends.vk.VKOAuth2',
    # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
)'''

#SOCIAL_AUTH_VK_OAUTH2_KEY = '7639343'
#SOCIAL_AUTH_VK_OAUTH2_SECRET = '1TsPm5huWtZBBPcKFivg'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysait.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "blog.context_processors.sponsors",
                # 'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysait.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'romashov$romashov_bd',
        'USER': 'romashov',
        'PASSWORD': '98201544Q',
        'HOST': 'romashov.mysql.pythonanywhere-services.com',
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Vladivostok'  # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMINS = (('Ромашов Никита', 'nikitos1654@gmail.com'))
MANAGERS = (('Тот_же_Никита', 'nikita64800@gmail.com'),
            ('Ромашов Никита', 'nikitos165@gmail.com'))

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'RomashovSait@gmail.com'
EMAIL_HOST_PASSWORD = 'saitsaitsait'
DEFAULT_FROM_EMAIL = 'Никита Ромашов'
DEFAULT_TO_EMAIL = 'nikitos1654@gmail.com'

#LOGIN_REDIRECT_URL = 'blog:home'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = 'D:\stady\Django\mysait\static'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'D:\stady\Django\mysait\media'
