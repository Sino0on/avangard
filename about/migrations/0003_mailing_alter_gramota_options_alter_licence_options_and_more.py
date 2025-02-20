# Generated by Django 5.1.3 on 2025-01-19 14:08

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_application_comment'),
        ('objects', '0014_alter_advantage_created_at_alter_advantage_svg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email для рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.AlterModelOptions(
            name='gramota',
            options={'verbose_name': 'Грамота', 'verbose_name_plural': 'Грамоты'},
        ),
        migrations.AlterModelOptions(
            name='licence',
            options={'verbose_name': 'Лицензия', 'verbose_name_plural': 'Лицензии'},
        ),
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.AlterModelOptions(
            name='section1',
            options={'verbose_name': 'Раздел 1', 'verbose_name_plural': 'Разделы 1'},
        ),
        migrations.AlterModelOptions(
            name='section2',
            options={'verbose_name': 'Раздел 2', 'verbose_name_plural': 'Разделы 2'},
        ),
        migrations.AlterModelOptions(
            name='section3',
            options={'verbose_name': 'Раздел 3', 'verbose_name_plural': 'Разделы 3'},
        ),
        migrations.AlterModelOptions(
            name='section4',
            options={'verbose_name': 'Раздел 4', 'verbose_name_plural': 'Разделы 4'},
        ),
        migrations.AlterModelOptions(
            name='section5',
            options={'verbose_name': 'Раздел 5', 'verbose_name_plural': 'Разделы 5'},
        ),
        migrations.AlterModelOptions(
            name='section6',
            options={'verbose_name': 'Раздел 6', 'verbose_name_plural': 'Разделы 6'},
        ),
        migrations.AlterModelOptions(
            name='sertificat',
            options={'verbose_name': 'Сертификат', 'verbose_name_plural': 'Сертификаты'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='advantages',
            field=models.ManyToManyField(to='objects.advantage', verbose_name='Преимущества'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='youtube_url_1',
            field=models.URLField(verbose_name='Ссылка на YouTube 1'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='youtube_url_2',
            field=models.URLField(verbose_name='Ссылка на YouTube 2'),
        ),
        migrations.AlterField(
            model_name='application',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=123, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=123, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='application',
            name='theme',
            field=models.CharField(blank=True, max_length=123, null=True, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='gramota',
            name='image',
            field=models.FileField(upload_to='images/gramotas/', verbose_name='Изображение грамоты'),
        ),
        migrations.AlterField(
            model_name='gramota',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.section4', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='gramota',
            name='title',
            field=models.CharField(max_length=123, verbose_name='Заголовок грамоты'),
        ),
        migrations.AlterField(
            model_name='licence',
            name='image',
            field=models.FileField(upload_to='images/licence/', verbose_name='Изображение лицензии'),
        ),
        migrations.AlterField(
            model_name='licence',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.section5', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='licence',
            name='title',
            field=models.CharField(max_length=123, verbose_name='Заголовок лицензии'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.section2', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='title',
            field=models.CharField(max_length=244, verbose_name='Заголовок материала'),
        ),
        migrations.AlterField(
            model_name='section1',
            name='about_us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_1', to='about.aboutus', verbose_name='О нас'),
        ),
        migrations.AlterField(
            model_name='section1',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='section2',
            name='about_us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_2', to='about.aboutus', verbose_name='О нас'),
        ),
        migrations.AlterField(
            model_name='section2',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='section3',
            name='about_us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_3', to='about.aboutus', verbose_name='О нас'),
        ),
        migrations.AlterField(
            model_name='section3',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='section4',
            name='about_us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_4', to='about.aboutus', verbose_name='О нас'),
        ),
        migrations.AlterField(
            model_name='section4',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='section5',
            name='about_us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_5', to='about.aboutus', verbose_name='О нас'),
        ),
        migrations.AlterField(
            model_name='section5',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='section5',
            name='title',
            field=models.CharField(max_length=123, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='section6',
            name='about_us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section_6', to='about.aboutus', verbose_name='О нас'),
        ),
        migrations.AlterField(
            model_name='section6',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='section6',
            name='title',
            field=models.CharField(max_length=123, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='sertificat',
            name='image',
            field=models.FileField(upload_to='images/licence/', verbose_name='Изображение сертификата'),
        ),
        migrations.AlterField(
            model_name='sertificat',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.section6', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='sertificat',
            name='title',
            field=models.CharField(max_length=123, verbose_name='Заголовок сертификата'),
        ),
    ]
