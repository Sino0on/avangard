# Generated by Django 5.1.3 on 2025-01-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_linknews"),
    ]

    operations = [
        migrations.AlterField(
            model_name="linknews",
            name="image",
            field=models.FileField(
                upload_to="images/link_news/", verbose_name="Изображение"
            ),
        ),
    ]
