from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _

from common.models import UuidMixin


class UserManager(BaseUserManager):
    def _create_user(self, email: str, password: str, **extra_fields) -> "User":
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields) -> "User":
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, UuidMixin):
    class Meta:
        abstract = False
        verbose_name = "user"
        verbose_name_plural = "users"

    username = None
    email = EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()
