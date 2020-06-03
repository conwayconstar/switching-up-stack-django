from djongo import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    Set username field to 'email'.
    Set required fields 'first_name'.
    Overwrite objects with our custom user manager.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profile_title = models.CharField(
        max_length=100,
        blank=True,
        default='What I\'m doing')
    profile_description = models.TextField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
