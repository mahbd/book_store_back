from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.URLField(blank=True, null=True)
