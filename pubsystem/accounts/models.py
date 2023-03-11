from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Account(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = "accounts"

    email = models.EmailField(verbose_name="メールアドレス", unique=True)

    REQUIRED_FIELDS = ("username",)
    USERNAME_FIELD = "email"
