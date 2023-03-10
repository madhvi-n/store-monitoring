import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_monitoring.settings')

app = Celery('store_monitoring')
app.conf.task_default_queue = 'store_monitoring_queue'
app.conf.task_default_exchange = 'store_monitoring_exchange'
app.conf.task_default_routing_key = 'store_monitoring'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
