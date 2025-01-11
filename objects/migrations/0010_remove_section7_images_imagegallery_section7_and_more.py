# Generated by Django 5.1.3 on 2025-01-11 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("objects", "0009_remove_section11_etaps_url_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="section7",
            name="images",
        ),
        migrations.AddField(
            model_name="imagegallery",
            name="section7",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="section_images",
                to="objects.section7",
            ),
        ),
        migrations.AlterField(
            model_name="building",
            name="mini_title",
            field=models.CharField(max_length=123, verbose_name="Серия"),
        ),
        migrations.AlterField(
            model_name="building",
            name="status",
            field=models.CharField(
                choices=[
                    ("active", "В процессе"),
                    ("archive", "Архив"),
                    ("ended", "Реализовано"),
                ],
                max_length=123,
                verbose_name="Статус",
            ),
        ),
    ]
