from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import reciever
from .models import UserProfile

@reciever(post_save, sender=User)
def create_user_profile(sender, insatnce, created, **keargs):
    if created:
        UserProfile.objects.create(user=instance)

@reciever(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.UserProfile.save()        