from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Image


# Django signals are synchronous and blocking
# attach the receiver to the m2m_changed and connect to the sender function
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
