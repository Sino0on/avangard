# Generated by Django 5.1.3 on 2025-01-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0008_alter_constructionprogress_month_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section11',
            name='etaps_url',
        ),
        migrations.RemoveField(
            model_name='section2',
            name='max_apartment',
        ),
        migrations.AddField(
            model_name='section1',
            name='max_apartment',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section1',
            name='second_image',
            field=models.ImageField(default=1, upload_to='images/buildings/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section10',
            name='location_iframe_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section2',
            name='first_image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section2',
            name='second_image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
