from __future__ import absolute_import
from django.conf import settings

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
BASE_PATH = os.path.dirname(os.path.abspath('manage.py'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

app = Celery('dashboard')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = settings.TIME_ZONE
app.conf.broker_url = settings.CELERY_BROKER_URL


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
