from tkinter import Image
from turtledemo.sorting_animate import Block

from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from django.utils.functional import cached_property


class InterestingNearby(models.Model):
    title = models.CharField(max_length=123, verbose_name="Название")
    image = models.ImageField(upload_to='images/other/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'
        ordering = ['-created_at']


# Жилой комплекс или резиденция итд
class Category(models.Model):
    title = models.CharField(max_length=123, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Advantage(models.Model):
    title = models.CharField(max_length=123, verbose_name="Название")
    svg = models.FileField(upload_to='svg/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['-created_at']



class Building(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='Слаг')
    title = models.CharField(max_length=123, verbose_name='Название')
    mini_title = models.CharField(max_length=123, verbose_name='Серия')
    status = models.CharField(max_length=123, choices=(
        ("active", "В процессе"),
        ("archive", "Архив"),
        ("ended", "Реализовано"),
    ), verbose_name='Статус')
    banner = models.FileField(upload_to='images/banners/', verbose_name="Видео")
    banner_img = models.FileField(upload_to='images/banners/', blank=True, null=True, verbose_name="Изображение")
    imagepng = models.ImageField(upload_to='images/bgs/', blank=True, null=True, verbose_name="Изображение PNG")
    imagebg = models.ImageField(upload_to='images/bgs/', verbose_name="Фоновое изображение")
    buklet = models.FileField(upload_to='files/buklets/', verbose_name="Буклет")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    is_new = models.BooleanField(default=False, verbose_name="Новинка")

    # section 1

    # section 2

    # section 3

    # section 4

    # section 5

    # section 6

    # section 7

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(unidecode(self.title))
            unique_slug = base_slug
            counter = 1
            while Building.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class InterestingNearbyBuilding(models.Model):
    time = models.CharField(max_length=123, verbose_name="Время от обьекта")
    building = models.ForeignKey(InterestingNearby, models.PROTECT, related_name='interetes', verbose_name="Объект")

    def __str__(self):
        return f'{self.building}'

    class Meta:
        verbose_name = 'Интересное место для объекта'
        verbose_name_plural = 'Интересные места для объектов'


class Section1(models.Model):
    first_image = models.ImageField(upload_to='images/buildings/', verbose_name="Первое изображение")
    second_image = models.ImageField(upload_to='images/buildings/', verbose_name="Второе изображение")
    description = models.TextField(verbose_name="Описание")
    address = models.CharField(max_length=123, verbose_name="Адрес")
    max_blocks = models.IntegerField(verbose_name="Блоки")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_1', verbose_name="Объект")
    max_apartment = models.IntegerField(verbose_name="Аппартаменты")

    class Meta:
        verbose_name = 'О комплексе'
        verbose_name_plural = 'О комплексе'


class Section2(models.Model):
    plot_area = models.FloatField(verbose_name="Площадь участка")
    parking_spaces = models.IntegerField(verbose_name="Парковочных мест")
    low_rise_blocks = models.IntegerField(verbose_name="Малоэтажных блоков")
    construction_area = models.IntegerField(verbose_name="Площадь застройки")
    appartament_quantity = models.IntegerField(verbose_name="Количество квартир")
    yard_area = models.FloatField(verbose_name="Площадь двора")
    green_area = models.FloatField(verbose_name="Площадь озеленения")
    childrens_playgrounds = models.IntegerField(verbose_name="Детских площадок")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_2', verbose_name="Объект")
    first_image = models.ImageField(upload_to='images', verbose_name="Первое изображение")
    second_image = models.ImageField(upload_to='images', verbose_name="Второе изображение")

    class Meta:
        verbose_name = 'В цифрах'
        verbose_name_plural = 'В цифрах'


class Section3(models.Model):
    day_image = models.ImageField(upload_to='images/buildings/', verbose_name="Дневное изображение")
    night_image = models.ImageField(upload_to='images/buildings/', verbose_name="Ночное изображение")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_3', verbose_name="Объект")

    class Meta:
        verbose_name = 'День и Ночь'
        verbose_name_plural = 'День и Ночь'


class Section4(models.Model):
    floorschemas = models.ManyToManyField('FloorSchema', verbose_name="Схема этажей")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_4', verbose_name="Объект")

    class Meta:
        verbose_name = 'Планы этажей'
        verbose_name_plural = 'Планы этажей'


class Section5(models.Model):
    under_parking_layout = models.ImageField(upload_to='images/buildings/', verbose_name="Подземная парковка")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_5', verbose_name="Объект")

    class Meta:
        verbose_name = 'Подземная парковка'
        verbose_name_plural = 'Подземная парковка'


class Section6(models.Model):
    architecture = models.ManyToManyField('Architecture', verbose_name="Архитектура")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_6', verbose_name="Объект")

    class Meta:
        verbose_name = 'Архитектура'
        verbose_name_plural = 'Архитектура'


class Section7(models.Model):
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_7', verbose_name="Объект")

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'


class Section8(models.Model):
    advantages = models.ManyToManyField(Advantage, verbose_name="Преимущества")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_8', verbose_name="Объект")

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'


class Section9(models.Model):
    interest_nearby = models.ManyToManyField(InterestingNearbyBuilding, verbose_name="Интересные места")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_9', verbose_name="Объект")

    class Meta:
        verbose_name = 'Интересное рядом'
        verbose_name_plural = 'Интересное рядом'


class Section10(models.Model):
    location_description = models.TextField(verbose_name="Описание локации")
    location_iframe_url = models.TextField(verbose_name="Ссылка адреса")
    location_image_first = models.ImageField(upload_to='images/buildings/', verbose_name="Первое изображение")
    location_image_second = models.ImageField(upload_to='images/buildings/', verbose_name="Второе изображение")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_10', verbose_name="Объект")

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локация'


class Section11(models.Model):
    youtube_url = models.URLField(verbose_name="")
    live_url = models.URLField(verbose_name="")
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_11', verbose_name="Объект")

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='images/gallery/', verbose_name="Изображение")
    section7 = models.ForeignKey(Section7, related_name='section_images', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Объект")


class FloorSchema(models.Model):
    title = models.CharField(max_length=123, verbose_name="Название")
    blocks = models.ManyToManyField("BlockInfo", verbose_name="Блоки")

    class Meta:
        verbose_name = 'Планировка этажа'
        verbose_name_plural = 'Планировки этажей'


class BlockInfo(models.Model):
    title = models.CharField(max_length=211, verbose_name="Название")
    image = models.ImageField(upload_to='images/buildings/', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Architecture(models.Model):
    title = models.CharField(max_length=123, verbose_name="Название")
    features = models.ManyToManyField('Features', verbose_name="Фича")

    class Meta:
        verbose_name = 'Архитектура'
        verbose_name_plural = 'Архитектура'

class Features(models.Model):
    title = models.CharField(max_length=123, verbose_name="Название")
    mini_description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Функция'
        verbose_name_plural = 'Функции'


class ConstructionProgress(models.Model):
    MONTH_CHOICES = [
        (1, "Январь"),
        (2, "Февраль"),
        (3, "Март"),
        (4, "Апрель"),
        (5, "Май"),
        (6, "Июнь"),
        (7, "Июль"),
        (8, "Август"),
        (9, "Сентябрь"),
        (10, "Октябрь"),
        (11, "Ноябрь"),
        (12, "Декабрь"),
    ]
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name="construction_progress",
        verbose_name="Здание"
    )
    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES,
        verbose_name="Месяц"
    )
    year = models.PositiveIntegerField(
        choices=[(i, f"{i:02d}") for i in range(2010, 2070)],
        verbose_name="Год"
    )

    class Meta:
        verbose_name = "Динамика строительства"
        verbose_name_plural = "Динамика строительства"
        ordering = ['-year', '-month']  # Сортировка по году и месяцу

    def __str__(self):
        return f"{self.building} - {self.get_month_display()} {self.year}"

class ConstructionProgressImage(models.Model):
    construction_progress = models.ForeignKey(
        ConstructionProgress,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Динамика строительства"
    )
    image = models.ImageField(
        upload_to="images/construction_progress/",
        verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Изображение динамики строительства"
        verbose_name_plural = "Изображения динамики строительства"

    def __str__(self):
        return f"Изображение для {self.construction_progress}"
