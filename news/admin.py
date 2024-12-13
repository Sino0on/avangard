from django.contrib import admin
from .models import News, NewsImages, LinkNews


class NewsImagesInline(admin.TabularInline):
    model = NewsImages
    extra = 1  # Количество пустых полей для добавления изображений
    readonly_fields = ['image_preview']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'slug', 'main_image')
    search_fields = ('title', 'description')
    inlines = [NewsImagesInline]  # Добавляем inline для изображений

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'youtube_link', 'main_image')
        }),
    )

@admin.register(NewsImages)
class NewsImagesAdmin(admin.ModelAdmin):
    list_display = ('news', 'image')
    search_fields = ('news__title',)
    readonly_fields = ['image_preview']


@admin.register(LinkNews)
class LinkNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'image')
    search_fields = ('title', 'url')
    list_filter = ('created_at',)
