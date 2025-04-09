"""
This module contains the User model which extends Django's AbstractUser model.
It customizes the authentication to use email as the primary identifier instead
of username.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    Extends the default Django User model to include an email field.
    """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """
        returns the email of the user
        """
        return self.email
