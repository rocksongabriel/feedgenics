from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        """Creates and saves a normal user"""
        user = self._create_user(email=email, password=password, **kwargs)

        return user

    def create_superuser(self, email, password=None):
        """Creates and saves a superuser"""
        user = self._create_user(email, password=password)
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("Email"), max_length=300, unique=True, blank=False, null=False
    )
    full_name = models.CharField(_("Full Name"), max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
