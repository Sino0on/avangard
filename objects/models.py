from tkinter import Image
from turtledemo.sorting_animate import Block

from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from django.utils.functional import cached_property


class InterestingNearby(models.Model):
    title = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/other/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'
        ordering = ['-created_at']


# Жилой комплекс или резиденция итд
class Category(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Advantage(models.Model):
    title = models.CharField(max_length=123)
    svg = models.FileField(upload_to='svg/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['-created_at']



class Building(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='Слаг')
    title = models.CharField(max_length=123, verbose_name='Название')
    mini_title = models.CharField(max_length=123)
    status = models.CharField(max_length=123, choices=(
        ("active", "В процессе"),
        ("archive", "Архив"),
        ("ended", "Реализовано"),
    ))
    banner = models.FileField(upload_to='images/banners/')
    buklet = models.FileField(upload_to='files/buklets/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

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
    time = models.CharField(max_length=123)
    building = models.ForeignKey(InterestingNearby, models.PROTECT, related_name='interetes')

    def __str__(self):
        return f'{self.building}'

    class Meta:
        verbose_name = 'Интересное место для объекта'
        verbose_name_plural = 'Интересные места для объектов'


class Section1(models.Model):
    first_image = models.ImageField(upload_to='images/buildings/')
    description = models.TextField()
    address = models.CharField(max_length=123)
    max_blocks = models.IntegerField()
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_1')

    class Meta:
        verbose_name = 'О комплексе'
        verbose_name_plural = 'О комплексе'


class Section2(models.Model):
    max_apartment = models.IntegerField()
    plot_area = models.FloatField()
    parking_spaces = models.IntegerField()
    low_rise_blocks = models.IntegerField()
    construction_area = models.IntegerField()
    appartament_quantity = models.IntegerField()
    yard_area = models.FloatField()
    green_area = models.FloatField()
    childrens_playgrounds = models.IntegerField()
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_2')

    class Meta:
        verbose_name = 'В цифрах'
        verbose_name_plural = 'В цифрах'


class Section3(models.Model):
    day_image = models.ImageField(upload_to='images/buildings/')
    night_image = models.ImageField(upload_to='images/buildings/')
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_3')

    class Meta:
        verbose_name = 'День и Ночь'
        verbose_name_plural = 'День и Ночь'


class Section4(models.Model):
    floorschemas = models.ManyToManyField('FloorSchema')
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_4')

    class Meta:
        verbose_name = 'Планы этажей'
        verbose_name_plural = 'Планы этажей'


class Section5(models.Model):
    under_parking_layout = models.ImageField(upload_to='images/buildings/')
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_5')

    class Meta:
        verbose_name = 'Подземная парковка'
        verbose_name_plural = 'Подземная парковка'

class Section6(models.Model):
    architecture = models.ManyToManyField('Architecture')
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_6')

    class Meta:
        verbose_name = 'Архитектура'
        verbose_name_plural = 'Архитектура'

class Section7(models.Model):
    images = models.ManyToManyField('ImageGallery')
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_7')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

class Section8(models.Model):
    advantages = models.ManyToManyField(Advantage)
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_8')

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'


class Section9(models.Model):
    interest_nearby = models.ManyToManyField(InterestingNearbyBuilding)
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_9')

    class Meta:
        verbose_name = 'Интересное рядом'
        verbose_name_plural = 'Интересное рядом'


class Section10(models.Model):
    location_description = models.TextField()
    location_image_first = models.ImageField(upload_to='images/buildings/')
    location_image_second = models.ImageField(upload_to='images/buildings/')
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_10')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локация'


class Section11(models.Model):
    youtube_url = models.URLField()
    live_url = models.URLField()
    etaps_url = models.URLField()
    building = models.OneToOneField(Building, on_delete=models.CASCADE, related_name='section_11')

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='images/gallery/')


class FloorSchema(models.Model):
    title = models.CharField(max_length=123)
    blocks = models.ManyToManyField("BlockInfo")

    class Meta:
        verbose_name = 'Планировка этажа'
        verbose_name_plural = 'Планировки этажей'


class BlockInfo(models.Model):
    title = models.CharField(max_length=211)
    image = models.ImageField(upload_to='images/buildings/')

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Architecture(models.Model):
    title = models.CharField(max_length=123)
    features = models.ManyToManyField('Features')

    class Meta:
        verbose_name = 'Архитектура'
        verbose_name_plural = 'Архитектура'

class Features(models.Model):
    title = models.CharField(max_length=123)
    mini_description = models.TextField()

    class Meta:
        verbose_name = 'Функция'
        verbose_name_plural = 'Функции'
