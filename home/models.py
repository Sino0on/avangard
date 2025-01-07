from django.db import models
from info.models import SingletonModel
from ckeditor.fields import RichTextField


class HomeInfo(SingletonModel):
    banner = models.FileField(upload_to='files/')
    first_key = models.CharField(max_length=123)
    second_key = models.CharField(max_length=123)
    third_key = models.CharField(max_length=123)
    first_value = models.CharField(max_length=123)
    second_value = models.CharField(max_length=123)
    third_value = models.CharField(max_length=123)
    address = RichTextField()

    def __str__(self):
        return 'Домашняя страница'

    class Meta:
        verbose_name = "Домашняя страница"
        verbose_name_plural = "Домашняя страница"

