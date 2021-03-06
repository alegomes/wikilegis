from django.core.exceptions import ObjectDoesNotExist
from django.template import Library
from notification.models import Newsletter

register = Library()


@register.assignment_tag()
def subscriber(bill_id, user_id):
    try:
        newsletter = Newsletter.objects.get(bill_id=bill_id, user_id=user_id)
        return newsletter.is_active
    except ObjectDoesNotExist:
        return False
