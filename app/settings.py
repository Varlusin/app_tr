import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-+c6v+b%n#bqi93=nf359n0i0ox!0qzxi6#69!2t6f4*r=p9t)$'

DEBUG = True
ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.postgres',
    'django.contrib.gis',

    "debug_toolbar",
    'phone_field',
    'django_extensions', ## սա այդքան էլ կարևոր բան չէ script աշխատացնելու համար է։
    'leaflet',

    'users',
    'mayin',
    'grups',
    'location',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', ##lenguage
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

 



ROOT_URLCONF = 'app.urls'

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



WSGI_APPLICATION = 'app.wsgi.application'



DATABASES = {
     'default': {
         "ENGINE": "django.contrib.gis.db.backends.postgis",
         'HOST': os.environ.get('DB_HOST'),
         'NAME': os.environ.get('DB_NAME'),
         'USER': os.environ.get('DB_USER'),
         'PASSWORD': os.environ.get('DB_PASS')
     }
 }




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




LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russia')),
    ('hy', gettext('Armenian')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'hy')


STATIC_URL = "/static/"
# STATIC_DIR = '/static/' ## locale
STATIC_ROOT = os.path.join(BASE_DIR, "static")

## locale translete lenguage files
LOCALE_PATHS = [
    BASE_DIR / "locale/",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# for costum user
AUTH_USER_MODEL = "users.CustomUser"

INTERNAL_IPS = [
    # ...
    # ...
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


LEAFLET_CONFIG = {
    "DEFAULT_CENTER" : (40.785273, 43.841774),
    "DEFAULT_ZOOM" : 13,
    "MAX_ZOOM" : 20,
    "MIN_ZOOM" : 10,
    "ATTRIBUTION_CONTROL": False,
    "ATTRIBUTION_PREFIX" : "My Custome Leaflet map"
}
