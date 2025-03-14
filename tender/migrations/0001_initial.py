# Generated by Django 5.1.3 on 2025-01-19 14:08

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('mini_description', models.TextField(verbose_name='Краткое описание')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('created_at', models.DateField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Тендер',
                'verbose_name_plural': 'Тендеры',
            },
        ),
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('file', models.FileField(upload_to='more_info_files/', verbose_name='Файл')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='more_infos', to='tender.tender', verbose_name='Тендер')),
            ],
            options={
                'verbose_name': 'Дополнительная информация',
                'verbose_name_plural': 'Дополнительная информация',
            },
        ),
        migrations.CreateModel(
            name='TenderApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('inn', models.CharField(max_length=20, verbose_name='ИНН')),
                ('yur_address', models.CharField(max_length=255, verbose_name='Юридический адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Телефон')),
                ('theme', models.CharField(max_length=255, verbose_name='Тема')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('comment_file', models.FileField(upload_to='application_files/', verbose_name='Файл комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='tender.tender', verbose_name='Тендер')),
            ],
            options={
                'verbose_name': 'Заявка на тендер',
                'verbose_name_plural': 'Заявки на тендеры',
                'ordering': ['-created_at'],
            },
        ),
    ]
