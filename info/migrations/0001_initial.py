# Generated by Django 5.1.3 on 2024-12-13 14:49

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
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
                ("addresses", ckeditor.fields.RichTextField(verbose_name="Адреса")),
                ("requisites", ckeditor.fields.RichTextField(verbose_name="Реквизиты")),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
            },
        ),
        migrations.CreateModel(
            name="RequisitesInDollar",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "contacts",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dollar_requisites",
                        to="info.contacts",
                        verbose_name="Контакты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Реквизиты в долларах",
                "verbose_name_plural": "Реквизиты в долларах",
            },
        ),
        migrations.CreateModel(
            name="RequisitesInSom",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "contacts",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_requisites",
                        to="info.contacts",
                        verbose_name="Контакты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Реквизиты в сомах",
                "verbose_name_plural": "Реквизиты в сомах",
            },
        ),
        migrations.CreateModel(
            name="SalesOffice",
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
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "contacts",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sales_offices",
                        to="info.contacts",
                        verbose_name="Контакты",
                    ),
                ),
            ],
            options={
                "verbose_name": "Офис продаж",
                "verbose_name_plural": "Офисы продаж",
            },
        ),
    ]
