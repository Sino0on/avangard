from django.db import models


class InterestingNearby(models.Model):
    title = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/other/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


# Жилой комплекс или резиденция итд
class Categry(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Advantage(models.Model):
    title = models.CharField(max_length=123)
    svg = models.FileField(upload_to='svg/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Building(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    mini_title = models.CharField(max_length=123)
    banner = models.ImageField(upload_to='images/banners/')
    buklet = models.FileField(upload_to='files/buklets/')
    first_image = models.ImageField(upload_to='images/buildings/')
    description = models.TextField()
    address = models.CharField(max_length=123)
    max_blocks = models.IntegerField()
    max_apartment = models.IntegerField()
    plot_area = models.FloatField()
    parking_spaces = models.IntegerField()
    low_rise_blocks = models.IntegerField()
    construction_area = models.IntegerField()
    appartament_quantity = models.IntegerField()
    yard_area = models.FloatField()
    green_area = models.FloatField()
    childrens_playgrounds = models.IntegerField()
    day_image = models.ImageField(upload_to='images/buildings/')
    night_image = models.ImageField(upload_to='images/buildings/')
    under_parking_layout = models.ImageField(upload_to='images/buildings/')
    location_image_first = models.ImageField(upload_to='images/buildings/')
    location_image_second = models.ImageField(upload_to='images/buildings/')
    youtube_url = models.URLField()
    live_url = models.URLField()
    etaps_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']



class InterestingNearbyBuilding(models.Model):
    time = models.CharField(max_length=123)
    building = models.ForeignKey(Building, models.PROTECT, related_name='interetes')
    interesting_nearby = models.ForeignKey(InterestingNearby, models.PROTECT)

    def __str__(self):
        return f'{self.building} - {self.interesting_nearby}'




