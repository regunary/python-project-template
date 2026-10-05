SECRET_KEY = "replace-me"
DEBUG = True
ROOT_URLCONF = "project.urls"
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
    "apps.api",
]
MIDDLEWARE = []
ALLOWED_HOSTS = ["*"]
