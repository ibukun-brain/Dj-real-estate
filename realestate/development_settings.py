from .base_settings import *
import dj_database_url
SECRET_KEY = 'django-insecure-6tm*+yigbua2wq4()eer@jt#x+0umk+y23_y_lx$06huk0w9lg'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APPEND_SLASH = True

CSRF_TRUSTED_ORIGINS = ["http://*"]

X_FRAME_OPTIONS = "SAMEORIGIN"

DATABASES["default"] = dj_database_url.parse(
    f"sqlite:////{BASE_DIR.joinpath(BASE_DIR.name)}.db", conn_max_age=600,
)

DISABLE_SERVER_SIDE_CURSORS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# if not DEBUG:
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_ROOT = BASE_DIR / "assets"