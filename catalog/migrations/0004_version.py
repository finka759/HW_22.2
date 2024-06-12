# Generated by Django 5.0.6 on 2024-06-04 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version_number",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="введите номер версии",
                        verbose_name="номер версии",
                    ),
                ),
                (
                    "version_name",
                    models.CharField(
                        blank=True,
                        help_text="введите наименование версии",
                        max_length=50,
                        null=True,
                        verbose_name="номер версии",
                    ),
                ),
                (
                    "is_current_version",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        null=True,
                        verbose_name="актуальность версии",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="version_product",
                        to="catalog.product",
                        verbose_name="продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия продукта",
                "verbose_name_plural": "Версии продуктов",
                "ordering": ["version_number"],
            },
        ),
    ]