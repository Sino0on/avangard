from django.db import models
from ckeditor.fields import RichTextField
from info.models import SingletonModel
from objects.models import Advantage


class AboutUs(SingletonModel):
    description = models.TextField()
    advantages = models.ManyToManyField(Advantage)
    youtube_url_1 = models.URLField()
    youtube_url_2 = models.URLField()

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Section1(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_1')


class Section2(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_2')


class Materials(models.Model):
    title = models.CharField(max_length=244)
    section = models.ForeignKey(Section2, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Section3(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_3')


class Section4(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(verbose_name='Описание')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_4')


class Gramota(models.Model):
    title = models.CharField(max_length=123)
    image = models.FileField(upload_to='images/gramotas/')
    section = models.ForeignKey(Section4, on_delete=models.CASCADE)


class Section5(models.Model):
    title = models.CharField(max_length=123)
    description = RichTextField()
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_5')

class Licence(models.Model):
    title = models.CharField(max_length=123)
    image = models.FileField(upload_to='images/licence/')
    section = models.ForeignKey(Section5, on_delete=models.CASCADE)


class Section6(models.Model):
    title = models.CharField(max_length=123)
    description = RichTextField()
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='section_6')


class Sertificat(models.Model):
    title = models.CharField(max_length=123)
    image = models.FileField(upload_to='images/licence/')
    section = models.ForeignKey(Section6, on_delete=models.CASCADE)


class Application(models.Model):
    theme = models.CharField(max_length=123, blank=True, null=True)
    name = models.CharField(max_length=123)
    phone = models.CharField(max_length=123)
    comment = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class Mailing(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-created_at']
