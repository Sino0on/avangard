# Generated by Django 5.1.3 on 2025-03-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0035_alter_blockinfo_options_alter_floorschema_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='floorschema',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
