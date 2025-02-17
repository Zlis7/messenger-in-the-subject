from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from .tools import hash_text_sha256
from django.db import models

class MinUserManager(BaseUserManager):
    def create_user(self, email, password,  **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=hash_text_sha256(email), **extra_fields)
        user.uid = user.email[39] + user.email[48] + user.email[35] + user.email[53] + user.email[43]
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=hash_text_sha256(email))

class MinUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(default='anonim', max_length=21, null=True)
    email = models.CharField(unique=True, max_length=65, blank=False, null=False)
    uid = models.CharField(default='', unique=True, max_length=6, blank=False, null=False)
    password = models.CharField(max_length=257, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = MinUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "MinUser"
        verbose_name_plural = "MinUser"
