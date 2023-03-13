from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Account(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = "accounts"

    username = models.CharField(
        verbose_name="ユーザー名",
        max_length=32,
        unique=True,
        help_text="32文字以内の半角英数字、@/./+/-/_ が利用できます。",
        validators=(AbstractUser.username_validator,),
    )
    email = models.EmailField(verbose_name="メールアドレス", unique=True)
    last_login = models.DateTimeField(verbose_name="最終ログイン日時", blank=True, null=True)

    REQUIRED_FIELDS = ("username",)
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username
