from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = RichTextField(
        verbose_name="Описание"
    )
    youtube_link = models.URLField(
        blank=True, null=True,
        verbose_name="Ссылка на YouTube"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="Слаг"
    )
    main_image = models.ImageField(
        upload_to='images/news/main/',
        verbose_name="Главное изображение",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        """Автоматически генерирует слаг на основе заголовка"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @classmethod
    def get_latest_news(cls):
        """Возвращает 5 последних новостей"""
        return cls.objects.all()[:5]

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='news_images',
        verbose_name="Новость"
    )
    image = models.ImageField(
        upload_to='images/news/',
        verbose_name="Изображение"
    )

    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', self.image.url)
        return "Нет изображения"

    image_preview.short_description = "Миниатюра"

    def __str__(self):
        return f'{self.news} - {self.image.name}'


class LinkNews(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    url = models.URLField(verbose_name="URL")
    image = models.FileField(upload_to='images/link_news/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Ссылка на новость"
        verbose_name_plural = "Ссылки на новости"
        ordering = ['-created_at']

    def __str__(self):
        return self.title