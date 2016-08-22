# -*- encoding: utf-8 -*-
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#k36frmo&@$#tyx^tp9hwq9fy#5lm(z91yoil*v5vhkf_o#)y='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seguimiento',
    'main',
    # social
    'social.apps.django_app.default',
    # forms
    'materializecssform',
    #Perfiles
    'perfil',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'provision.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Python social auth
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'provision.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'danr2prfn23u59',
        'USER': 'jlheyklubhtdai',
        'PASSWORD': 'Sn4nyV3RKCsYJPUC5F8Ga_ZZON',
        'HOST': 'ec2-54-83-52-71.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES['default'] =  dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.join(BASE_DIR,"static"),)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

# Correo electronico
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'tterrenofacil@gmail.com'
EMAIL_HOST_PASSWORD = 'Miguel741010'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL=False

# Formato de fecha con materializecss
# USE_L10N=True
# DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

LOGIN_URL='_login'

from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('perfil:dashboard')


# Social auth
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',)

SOCIAL_AUTH_FACEBOOK_KEY="1623909724551044"
SOCIAL_AUTH_FACEBOOK_SECRET='9ae884ea1c34fbd2ae127b48096fea34'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email, age_range'
}

SOCIAL_AUTH_LOGIN_REDIRECT_URL="_home"

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    # 'usuarios.pipelines.save_profile_picture',  # <--- set the import-path to the function
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

#Celery Stuff LOCAL
# BROKER_URL='redis://localhost:6379'
# CELERY_RESULT_BACKEND='redis://localhost:6379'

# Celery Stuff Heroku
BROKER_URL='redis://h:p37plo67rvej6ef38ndjtsvhr91@ec2-107-21-254-141.compute-1.amazonaws.com:19289'
CELERY_RESULT_BACKEND='redis://h:p37plo67rvej6ef38ndjtsvhr91@ec2-107-21-254-141.compute-1.amazonaws.com:19289'
REDIS_URL='redis://h:p37plo67rvej6ef38ndjtsvhr91@ec2-107-21-254-141.compute-1.amazonaws.com:19289'



CELERY_ACCEPT_CONTENT=['application/json']
CELERY_TASK_SERIALIZER='json'
CELERY_RESULT_SERIALIZER='json'
CELERY_TIMEZONE='America/Mexico_City'




