from django.contrib import admin
from jazzmin.settings import THEMES

from .models import *
from django.utils.html import format_html
import nested_admin



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

class ImaegsInline(admin.StackedInline):
    model = ImageGallery
    extra = 1  # Количество пустых строк для добавления новых реквизитов
    fields = ['image']
    # verbose_name = "Реквизиты в сомах"
    # verbose_name_plural = "Реквизиты в сомах"


class Section7Inline(admin.StackedInline):
    model = Section7
    extra = 0

    # inlines = [ImaegsInline]

    # def images(self, obj):
    #     # Формируем список миниатюр всех изображений, связанных с Section4
    #     images = obj.gallery.all()  # Предполагаем, что gallery - это ManyToManyField
    #     if images:
    #         return format_html(' '.join(
    #             f'<img src="{image.image.url}" style="max-width: 100px; max-height: 100px; margin-right: 5px;" />'
    #             for image in images
    #         ))
    #     return "No images"
    #
    #
    # list_display = ['image']


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


class Section12Inline(admin.StackedInline):
    model = Section12
    extra = 0


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    # exclude = ['slug']
    inlines = [
        SectionInline,
        Section2Inline,
        Section3Inline,
        # Section4Inline,
        Section5Inline,
        # Section6Inline,
        # Section7Inline,
        Section8Inline,
        Section9Inline,
        Section10Inline,
        Section11Inline,
        Section12Inline,
    ]
    prepopulated_fields = {'slug': ('title',)}


class GalleryInline(admin.StackedInline):
    model = ImageGallery
    extra = 1


@admin.register(Section7)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline,
    ]


class FloorSchemaInline(admin.StackedInline):
    model = FloorSchema
    extra = 1


@admin.register(Section4)
class FloorSchemaAdmin(admin.ModelAdmin):
    inlines = [
        FloorSchemaInline,
    ]


class BlocksInline(admin.StackedInline):
    model = BlockInfo
    extra = 1


@admin.register(FloorSchema)
class FloorAdmin(admin.ModelAdmin):
    inlines = [
        BlocksInline,
    ]


class InterestingInline(admin.StackedInline):
    model = InterestingNearbyBuilding
    extra = 1


@admin.register(Section9)
class Section9Admin(admin.ModelAdmin):
    inlines = [
        InterestingInline,
    ]


class NumericInline(admin.StackedInline):
    model = Numeric
    extra = 1

@admin.register(Section2)
class FloorSchemaAdmin(admin.ModelAdmin):
    inlines = [
        NumericInline,
    ]

admin.site.register(Advantage)
admin.site.register(ThreeD)
# admin.site.register(FloorSchema)


@admin.register(ImageGallery)
class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ['image_tag', ]


class FeaturesInline(admin.StackedInline):
    model = Features
    extra = 1


@admin.register(Architecture)
class ArchitectureAdmin(admin.ModelAdmin):
    inlines = [
        FeaturesInline,
    ]


class ArchitectureInline(admin.StackedInline):
    model = Architecture
    extra = 1


@admin.register(Section6)
class Section6Admin(admin.ModelAdmin):
    inlines = [
        ArchitectureInline,
    ]


class ParkingImagesInline(admin.StackedInline):
    model = ParkingImages
    extra = 1


@admin.register(Section5)
class Section5Admin(admin.ModelAdmin):
    inlines = [
        ParkingImagesInline,
    ]


class ApartmentsInline(admin.StackedInline):
    model = Apartments
    extra = 1


@admin.register(Section1)
class Section1Admin(admin.ModelAdmin):
    inlines = [
        ApartmentsInline,
    ]


# admin.site.register(BlockInfo)
# admin.site.register(Architecture)
# admin.site.register(Features)
# admin.site.register(InterestingNearbyBuilding)
admin.site.register(InterestingNearby)
admin.site.register(Category)


class ConstructionProgressImageInline(admin.TabularInline):
    model = ConstructionProgressImage
    extra = 1  # Количество пустых строк для добавления изображений
    fields = ['image']
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"


@admin.register(ConstructionProgress)
class ConstructionProgressAdmin(admin.ModelAdmin):
    list_display = ('building', 'month', 'year')
    list_filter = ('year', 'month', 'building')
    search_fields = ('building__name',)
    inlines = [ConstructionProgressImageInline]

    # Настраиваем формы для выбора месяца и года
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "month":
            kwargs['choices'] = ConstructionProgress.MONTH_CHOICES
        return super().formfield_for_choice_field(db_field, request, **kwargs)
