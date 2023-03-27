import os
from celery import Celery

# Set an environment variable to point to our settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')

# Create a Celery instance with a name
celery = Celery('storefront')

# Specify where Celery can find configuration variables
celery.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from modules named tasks.py
celery.autodiscover_tasks()