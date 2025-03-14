# Generated by Django 5.1.3 on 2025-02-02 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tender", "0002_vacanciapplication_vacancies"),
    ]

    operations = [
        migrations.AddField(
            model_name="tender",
            name="file",
            field=models.FileField(
                default=1, upload_to="more_info_files/", verbose_name="Файл"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tender",
            name="organization",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Закупающая организация",
            ),
        ),
        migrations.AddField(
            model_name="tender",
            name="place",
            field=models.CharField(
                blank=True, max_length=123, null=True, verbose_name="место"
            ),
        ),
        migrations.AddField(
            model_name="tender",
            name="purpose",
            field=models.TextField(blank=True, null=True, verbose_name="Цель закупки"),
        ),
        migrations.AddField(
            model_name="tender",
            name="responsible_person",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Ответственный"
            ),
        ),
        migrations.AddField(
            model_name="tender",
            name="subject",
            field=models.TextField(
                blank=True, null=True, verbose_name="Предмет закупки"
            ),
        ),
        migrations.AddField(
            model_name="tender",
            name="supplier_selection_method",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Способ определения поставщика",
            ),
        ),
        migrations.AlterField(
            model_name="tender",
            name="created_at",
            field=models.DateField(blank=True, null=True, verbose_name="Дата создания"),
        ),
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("link", models.URLField(verbose_name="Ссылка")),
                (
                    "tender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tender.tender"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Requirement",
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
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название требования"
                    ),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="Количество")),
                (
                    "tender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tender.tender"
                    ),
                ),
            ],
        ),
    ]
