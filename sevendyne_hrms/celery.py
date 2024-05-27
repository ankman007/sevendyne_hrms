from celery import Celery

app = Celery('sevendyne_hrms')

# Set the default Django settings module for the 'celery' program.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Setting this configuration to address the warning
app.conf.broker_connection_retry_on_startup = True

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
