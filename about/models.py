from django.db import models
from ckeditor.fields import RichTextField
from info.models import SingletonModel
from objects.models import Advantage


class AboutUs(SingletonModel):
    description = models.TextField(verbose_name='Описание')
    advantages = models.ManyToManyField(Advantage, verbose_name='Преимущества')
    youtube_url_1 = models.URLField(verbose_name='Ссылка на YouTube 1')
    youtube_url_2 = models.URLField(verbose_name='Ссылка на YouTube 2')

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Section1(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_1', verbose_name='О нас')

    class Meta:
        verbose_name = 'Раздел 1'
        verbose_name_plural = 'Разделы 1'


class Section2(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_2', verbose_name='О нас')

    class Meta:
        verbose_name = 'Раздел 2'
        verbose_name_plural = 'Разделы 2'


class Materials(models.Model):
    title = models.CharField(max_length=244, verbose_name='Заголовок материала')
    section = models.ForeignKey(Section2, on_delete=models.CASCADE, verbose_name='Раздел')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Section3(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_3', verbose_name='О нас')

    class Meta:
        verbose_name = 'Раздел 3'
        verbose_name_plural = 'Разделы 3'


class Section4(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_4', verbose_name='О нас')

    class Meta:
        verbose_name = 'Раздел 4'
        verbose_name_plural = 'Разделы 4'


class Gramota(models.Model):
    title = models.CharField(max_length=123, verbose_name='Заголовок грамоты')
    image = models.FileField(upload_to='images/gramotas/', verbose_name='Изображение грамоты')
    section = models.ForeignKey(Section4, on_delete=models.CASCADE, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Грамота'
        verbose_name_plural = 'Грамоты'


class Section5(models.Model):
    title = models.CharField(max_length=123, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_5', verbose_name='О нас')

    class Meta:
        verbose_name = 'Раздел 5'
        verbose_name_plural = 'Разделы 5'


class Licence(models.Model):
    title = models.CharField(max_length=123, verbose_name='Заголовок лицензии')
    image = models.FileField(upload_to='images/licence/', verbose_name='Изображение лицензии')
    section = models.ForeignKey(Section5, on_delete=models.CASCADE, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'


class Section6(models.Model):
    title = models.CharField(max_length=123, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_6', verbose_name='О нас')

    class Meta:
        verbose_name = 'Раздел 6'
        verbose_name_plural = 'Разделы 6'


class Sertificat(models.Model):
    title = models.CharField(max_length=123, verbose_name='Заголовок сертификата')
    image = models.FileField(upload_to='images/licence/', verbose_name='Изображение сертификата')
    section = models.ForeignKey(Section6, on_delete=models.CASCADE, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Application(models.Model):
    theme = models.CharField(max_length=123, blank=True, null=True, verbose_name='Тема')
    name = models.CharField(max_length=123, verbose_name='Имя')
    phone = models.CharField(max_length=123, verbose_name='Телефон')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class Mailing(models.Model):
    email = models.EmailField(verbose_name='Email для рассылки')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
