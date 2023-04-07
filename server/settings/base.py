import os
from pathlib import Path
from .environ import env

DEBUG = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

BASE_URL = env("BASE_URL")

PROJECT_NAME = "Notice Server"

PROJECT_DIR = BASE_DIR / "server"

SECRET_KEY = "django-insecure-b(j+w&tmv6cq2&ufdo=@4(35-5qag-ahi6(gw(d^oaednfdo(h"

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://shorts.dev-tunnel.mitija.com",
]

SITE_ID = 1
SITE_DOMAIN = env("SITE_DOMAIN")

INSTALLED_APPS = [
    "apps",
    "auths",
    "shorts",
    "providers.authentics",
    "providers.authentics.api",
    # Dependencies
    "easy_thumbnails",
    "rest_framework",
    "rest_framework_api_key",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "corsheaders",
    # Django
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_celery_results",
    "django_celery_beat",
    # Authentication
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_cleanup",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


##############################################################################
# DATABASE
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
##############################################################################

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

##############################################################################
# AUTHENTICATIONS
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
##############################################################################
USE_TLS = os.getenv("USE_TLS", False)

if USE_TLS:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"  # or https
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_ADAPTER = "auths.adapter.AccountAdapter"
ACCOUNT_FORMS = {
    "login": "allauth.account.forms.LoginForm",
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",
    # "signup": "auths.forms.SignupForm",
}


# Authentication Service
AUTHENTICS_BASEURL = "https://oauth2.dev-tunnel.mitija.com"
AUTHENTICS_API_KEY = env("AUTHENTICS_API_KEY", "")
AUTHENTICS_CLIENT_ID = env("AUTHENTICS_CLIENT_ID", "")
AUTHENTICS_CLIENT_SECRET = env("AUTHENTICS_CLIENT_SECRET", "")
AUTHENTICS_REDIRECT_URL = env("AUTHENTICS_REDIRECT_URL", "")
AUTHENTICS_API_URL = env("AUTHENTICS_API_URL", "")

# Provider specific settings
SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"
SOCIALACCOUNT_PROVIDERS = {
    "authentics": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": AUTHENTICS_CLIENT_ID,
            "secret": AUTHENTICS_CLIENT_SECRET,
            "key": "",
        }
    }
}

# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "auths.User"
AUTH_VALIDATORS = "django.contrib.auth.password_validation."
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": AUTH_VALIDATORS + "UserAttributeSimilarityValidator"},
    {"NAME": AUTH_VALIDATORS + "MinimumLengthValidator"},
    {"NAME": AUTH_VALIDATORS + "CommonPasswordValidator"},
    {"NAME": AUTH_VALIDATORS + "NumericPasswordValidator"},
]


##############################################################################
# NOTIFICATIONS
##############################################################################


##############################################################################
# QUEUES
##############################################################################

# save Celery task results in Django's database
CELERY_RESULT_BACKEND = "django-db"

# This configures Redis as the datastore between Django + Celery
CELERY_BROKER_URL = env("CELERY_BROKER_REDIS_URL")
# if you out to use os.environ the config is:
# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_REDIS_URL', 'redis://localhost:6379')

CELERY_RESULT_EXTENDED = True

# this allows you to schedule items in the Django admin.
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"


##############################################################################
# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/4.0/topics/i18n/
##############################################################################

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Jakarta"
USE_I18N = True
USE_L10N = True
USE_TZ = True

##############################################################################
# STATICFILE & STORAGE
##############################################################################

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
MEDIA_URL = "/media/"

##############################################################################
# EMAIL
##############################################################################

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
