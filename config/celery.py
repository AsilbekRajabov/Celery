from __future__ import absolute_import
import os
from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.imports = ('apps.products.tasks', 'apps.tests.tasks')

app.conf.update(
    task_track_started=True,
)