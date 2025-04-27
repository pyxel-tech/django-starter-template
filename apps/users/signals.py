from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import Profile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)


"""
Quando tem dois tipos de usuários, pode ser tratado no formato abaixo:

if instance.is_customer and not hasattr(instance, 'customerprofile'):
    CustomerProfile.objects.create(user=instance)

if instance.is_merchant and not hasattr(instance, 'merchantprofile'):
    MerchantProfile.objects.create(user=instance)
"""
