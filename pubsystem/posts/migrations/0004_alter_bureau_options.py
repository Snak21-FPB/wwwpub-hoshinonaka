# Generated by Django 4.1.7 on 2023-03-13 08:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_alter_bureau_options_alter_bureau_created_by_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bureau",
            options={
                "ordering": ("sort_num",),
                "verbose_name": "局",
                "verbose_name_plural": "局リスト",
            },
        ),
    ]