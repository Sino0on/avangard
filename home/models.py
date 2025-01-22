from django.db import models
from info.models import SingletonModel, Contacts
from ckeditor.fields import RichTextField


class HomeInfo(SingletonModel):
    banner = models.FileField(upload_to='files/')
    first_key = models.CharField(max_length=123)
    second_key = models.CharField(max_length=123)
    third_key = models.CharField(max_length=123)
    first_value = models.IntegerField(default=0)
    second_value = models.IntegerField(default=0)
    third_value = models.IntegerField(default=0)

    def __str__(self):
        return 'Домашняя страница'

    class Meta:
        verbose_name = "Домашняя страница"
        verbose_name_plural = "Домашняя страница"


class Address(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=255)
    home = models.ForeignKey(HomeInfo, on_delete=models.CASCADE, related_name='addresses')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='addresss', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
