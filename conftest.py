import os, sys
from django.conf import settings


def pytest_configure():
    sys.path.append(os.path.dirname(__file__))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
