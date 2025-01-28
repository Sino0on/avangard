from django.db import models
from ckeditor.fields import RichTextField

from info.models import SingletonModel


class Tender(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    mini_description = models.TextField(verbose_name="Краткое описание")
    description = RichTextField(verbose_name="Описание")
    created_at = models.DateField(verbose_name="Дата создания")

    class Meta:
        verbose_name = "Тендер"
        verbose_name_plural = "Тендеры"

    def __str__(self):
        return self.title


class MoreInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    link = models.URLField(verbose_name="Ссылка")
    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE,
        related_name="more_infos",
        verbose_name="Тендер"
    )
    file = models.FileField(upload_to='more_info_files/', verbose_name="Файл")

    class Meta:
        verbose_name = "Дополнительная информация"
        verbose_name_plural = "Дополнительная информация"

    def __str__(self):
        return self.title


class TenderApplication(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Название компании")
    inn = models.CharField(max_length=20, verbose_name="ИНН")
    yur_address = models.CharField(max_length=255, verbose_name="Юридический адрес")
    email = models.EmailField(verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=15, verbose_name="Телефон")
    theme = models.CharField(max_length=255, verbose_name="Тема")
    comment = models.TextField(verbose_name="Комментарий")
    comment_file = models.FileField(upload_to='application_files/', verbose_name="Файл комментария")
    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="Тендер"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка на тендер"
        verbose_name_plural = "Заявки на тендеры"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.company_name} на тендер {self.tender.title}"


class Vacancies(SingletonModel):
    usloviya = RichTextField(verbose_name='Условия работы')
    phone = models.CharField(max_length=123, verbose_name='Номер телефона')

    def __str__(self):
        return 'Вакансии'

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"


class VacanciApplication(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Название компании")
    phone = models.CharField(max_length=123, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name="Электронная почта")
    comment = models.TextField(verbose_name="Комментарий")
    csv = models.FileField(upload_to='application_files/', verbose_name="Резюме")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка вакансии"
        verbose_name_plural = "Заявки вакансии"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.fullname}"
