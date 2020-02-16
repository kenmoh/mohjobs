from django.db.models.signals import post_save
from .models import User, UserProfile
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        user_profile = UserProfile(user=user)
        user_profile.save()
