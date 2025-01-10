from django.db import models
from ckeditor.fields import RichTextField

class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.id:
            existing = self.__class__.objects.first()
            for field in self._meta.fields:
                if field.name != 'id':
                    setattr(existing, field.name, getattr(self, field.name))
            existing.save()
        else:
            super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class Contacts(SingletonModel):
    addresses = RichTextField(verbose_name="Адреса")
    requisites = RichTextField(verbose_name="Реквизиты")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return "Контакты"


class SalesOffice(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    contacts = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        related_name="sales_offices",
        verbose_name="Контакты"
    )

    class Meta:
        verbose_name = "Офис продаж"
        verbose_name_plural = "Офисы продаж"

    def __str__(self):
        return self.name

class RequisitesInSom(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    contacts = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        related_name="som_requisites",
        verbose_name="Контакты"
    )

    class Meta:
        verbose_name = "Реквизиты в сомах"
        verbose_name_plural = "Реквизиты в сомах"

    def __str__(self):
        return self.title

class RequisitesInDollar(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    contacts = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        related_name="dollar_requisites",
        verbose_name="Контакты"
    )

    class Meta:
        verbose_name = "Реквизиты в долларах"
        verbose_name_plural = "Реквизиты в долларах"

    def __str__(self):
        return self.title

from django.db import models
from ckeditor.fields import RichTextField

class TechnicalBase(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Описание")
    youtube_url = models.URLField(verbose_name="Ссылка на YouTube", blank=True, null=True)

    class Meta:
        verbose_name = "Техническая база"
        verbose_name_plural = "Техническая база"

    def __str__(self):
        return "Техническая база"


class TechnicalBaseImage(models.Model):
    technical_base = models.ForeignKey(
        TechnicalBase,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Техническая база"
    )
    image = models.ImageField(upload_to='images/technical_base/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение технической базы"
        verbose_name_plural = "Изображения технической базы"

    def __str__(self):
        return f"{self.technical_base} - Изображение"