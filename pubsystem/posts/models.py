from django.contrib.auth import get_user_model
from django.db import models
from markdownx.models import MarkdownxField


class Bureau(models.Model):
    class Meta:
        db_table = "bureaus"

    name = models.CharField(verbose_name="名称", max_length=16, unique=True)
    keyword = models.SlugField(
        verbose_name="キーワード", unique=True, help_text="英数字と-が利用できます。URLに使用される文字列です。"
    )
    outline = MarkdownxField("局概要", help_text="マークダウン形式で入力してください。")
    sort_num = models.SmallIntegerField(
        verbose_name="ソート値", help_text="整数を入力してください。値が小さいほど上に表示されます。"
    )
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="bureau_creator",
        null=True,
        editable=False,
    )
    updated_at = models.DateTimeField(verbose_name="最終更新日時", auto_now=True)
    updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="bureau_updater",
        null=True,
        editable=False,
    )
