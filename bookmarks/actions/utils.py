import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action


# Shortcut to create action
def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    # Avoid saving duplicated action
    similar_actions = Action.objects.filter(
        user_id=user.id,
        verb=verb,
        created__gte=last_minute
    )
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
            target_ct=target_ct,
            target_id=target.id
        )

        if not similar_actions:
            # no existing actions found
            action = Action(usr=user, verb=verb, target=target)
            action.save()
            return True

    return False
