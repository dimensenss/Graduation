from celery import shared_task
from celery_singleton import Singleton
from django.db.models import F


@shared_task(base=Singleton)
def set_sub_price(sub_id):
    from services.models import Subscription

    sub = Subscription.objects.filter(id=sub_id).annotate(
        annotated_price=(F('course__full_price') - (F('course__full_price') * F('plan__discount_percent') / 100))
    )[0]

    sub.price = sub.annotated_price
    sub.save(update_fields=['price'])
