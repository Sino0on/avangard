# Generated by Django 5.1.3 on 2025-01-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0012_building_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='banner_img',
            field=models.FileField(blank=True, null=True, upload_to='images/banners/'),
        ),
    ]
