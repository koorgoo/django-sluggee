DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = 'local'

INSTALLED_APPS = (
    'sluggee',
    'tests',
)
