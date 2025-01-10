from django.contrib import admin
from .models import Contacts, SalesOffice, RequisitesInSom, RequisitesInDollar

# Inline для Офисов продаж
class SalesOfficeInline(admin.TabularInline):
    model = SalesOffice
    extra = 1  # Количество пустых строк для добавления новых офисов
    fields = ['name', 'description']
    verbose_name = "Офис продаж"
    verbose_name_plural = "Офисы продаж"

# Inline для Реквизитов в сомах
class RequisitesInSomInline(admin.TabularInline):
    model = RequisitesInSom
    extra = 1  # Количество пустых строк для добавления новых реквизитов
    fields = ['title', 'description']
    verbose_name = "Реквизиты в сомах"
    verbose_name_plural = "Реквизиты в сомах"

# Inline для Реквизитов в долларах
class RequisitesInDollarInline(admin.TabularInline):
    model = RequisitesInDollar
    extra = 1  # Количество пустых строк для добавления новых реквизитов
    fields = ['title', 'description']
    verbose_name = "Реквизиты в долларах"
    verbose_name_plural = "Реквизиты в долларах"

# Админка для Контактов с inlines
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("addresses", "requisites")
    inlines = [SalesOfficeInline, RequisitesInSomInline, RequisitesInDollarInline]
    fieldsets = (
        (None, {
            "fields": ("addresses", "requisites")
        }),
    )


from django.contrib import admin
from .models import TechnicalBase, TechnicalBaseImage

class TechnicalBaseImageInline(admin.TabularInline):
    model = TechnicalBaseImage
    extra = 1  # Количество пустых строк для добавления новых изображений
    fields = ['image']
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"

@admin.register(TechnicalBase)
class TechnicalBaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url')
    fieldsets = (
        (None, {
            "fields": ("title", "description", "youtube_url")
        }),
    )
    inlines = [TechnicalBaseImageInline]