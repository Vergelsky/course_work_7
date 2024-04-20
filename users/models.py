from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# from rooster.models import NULLABLE


class User(AbstractUser):
    username = None
    tg_id = models.IntegerField(verbose_name='идентификатор пользователя телеграмм', blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
