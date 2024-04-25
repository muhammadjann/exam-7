from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

from apps.users.models import User


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        instance.activation_token = get_random_string(length=30)
        instance.save()
        subject = "Activate Your Account"
        message = render_to_string(
            "activation_email.html", {"token": instance.activation_token}
        )
        send_mail(subject, message, "from@example.com", [instance.email])
