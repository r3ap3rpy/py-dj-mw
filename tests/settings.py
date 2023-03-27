SECRET_KEY = "KEY"
ROOT_URLCONF = ""
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "demo_app"
]
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "dani-sql-tools.middleware.new_middleware"
]
DATABASES = {
    "default" : {
        "ENGINE":"django.db.backends.sqlite3"
    }
}
USE_TZ=False