from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# We doo that for create profile for each user

# @receiver permet d'etre à l'écoute, ce qui fait que pour qu'à chaque fois qu'il y a un signal sur un nouvel utilisateur créé, il puisse exécuter le code ci-dessous
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
