from celery import task
from decimal import Decimal
import logging

@task(queue="default")
def update_service(payload):
    try:
        from events.models import Services
        duration = payload.get('duration')
        if duration:
            duration = Decimal((payload.get('duration')/(10**9)))
        service, _ = Services.objects.update_or_create(
            owner_id=payload.get('owner_id'),
            label=payload.get('label'),
            host=payload.get('host'),
            defaults={
                'status': payload.get('status'),
                'tags': payload.get('tags'),
                'message': payload.get('message'),
                'duration': duration,
                'date_time': payload.get('date_time'),
            }
        )
    except Exception as ex:
        logging.error(ex, exc_info=True)
