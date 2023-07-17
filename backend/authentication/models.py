from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass
    is_owner = models.BooleanField('owner status', default=False)
    is_guest = models.BooleanField('guest status', default=False)