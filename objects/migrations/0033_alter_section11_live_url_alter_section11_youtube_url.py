# Generated by Django 5.1.3 on 2025-02-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("objects", "0032_alter_section10_location_image_first_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section11",
            name="live_url",
            field=models.URLField(verbose_name="Ссылка на лайф стрим"),
        ),
        migrations.AlterField(
            model_name="section11",
            name="youtube_url",
            field=models.URLField(verbose_name="Ссылка на ютуб"),
        ),
    ]
