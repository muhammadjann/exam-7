from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import AbstractModel


class User(AbstractModel, AbstractUser):
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    activation_token = models.CharField(max_length=100, blank=True)
