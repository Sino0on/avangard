from django.contrib import admin
from .models import *
from django.utils.html import format_html



class SectionInline(admin.StackedInline):
    model = Section1
    extra = 0

class Section2Inline(admin.StackedInline):
    model = Section2
    extra = 0

class Section3Inline(admin.StackedInline):
    model = Section3
    extra = 0

class Section4Inline(admin.StackedInline):
    model = Section4
    extra = 0
    filter_horizontal = ('floorschemas',)

class Section5Inline(admin.StackedInline):
    model = Section5
    extra = 0

class Section6Inline(admin.StackedInline):
    model = Section6
    extra = 0
    filter_horizontal = ('architecture',)

class Section7Inline(admin.StackedInline):
    model = Section7
    extra = 0
    filter_horizontal = ('images',)

    def images(self, obj):
        # Формируем список миниатюр всех изображений, связанных с Section4
        images = obj.gallery.all()  # Предполагаем, что gallery - это ManyToManyField
        if images:
            return format_html(' '.join(
                f'<img src="{image.image.url}" style="max-width: 100px; max-height: 100px; margin-right: 5px;" />'
                for image in images
            ))
        return "No images"


    list_display = ['images']


class Section8Inline(admin.StackedInline):
    model = Section8
    extra = 0
    filter_vertical = ('advantages',)


class Section9Inline(admin.StackedInline):
    model = Section9
    extra = 0


class Section10Inline(admin.StackedInline):
    model = Section10
    extra = 0


class Section11Inline(admin.StackedInline):
    model = Section11
    extra = 0


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    inlines = [
        SectionInline,
        Section2Inline,
        Section3Inline,
        Section4Inline,
        Section5Inline,
        Section6Inline,
        Section7Inline,
        Section8Inline,
        Section9Inline,
        Section10Inline,
        Section11Inline,
    ]




admin.site.register(Advantage)
admin.site.register(FloorSchema)

@admin.register(ImageGallery)
class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['image_tag', ]



@admin.register(Architecture)
class ArchitectureAdmin(admin.ModelAdmin):
    filter_vertical = ('advantages',)

admin.site.register(BlockInfo)
# admin.site.register(Architecture)
admin.site.register(Features)
admin.site.register(InterestingNearbyBuilding)
admin.site.register(InterestingNearby)
admin.site.register(Category)
