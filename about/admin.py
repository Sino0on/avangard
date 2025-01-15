import nested_admin
from django.contrib import admin
from .models import *
from django.utils.html import format_html



class SectionInline(nested_admin.NestedStackedInline):
    model = Section1
    extra = 0

class MaterialsInline(nested_admin.NestedStackedInline):
    model = Materials
    extra = 1  # Количество пустых форм для добавления

class Section2Inline(nested_admin.NestedStackedInline):
    model = Section2
    inlines = [MaterialsInline]
    extra = 0

class Section3Inline(nested_admin.NestedStackedInline):
    model = Section3
    extra = 0

class GramotaInline(nested_admin.NestedStackedInline):
    model = Gramota
    extra = 1  # Количество пустых форм для добавления

class Section4Inline(nested_admin.NestedStackedInline):
    model = Section4
    inlines = [GramotaInline]
    extra = 0

class LicenceInline(nested_admin.NestedStackedInline):
    model = Licence
    extra = 1  # Количество пустых форм для добавления

class Section5Inline(nested_admin.NestedStackedInline):
    model = Section5
    inlines = [LicenceInline]
    extra = 0


class Section6Inline(nested_admin.NestedStackedInline):
    model = Section6
    extra = 0


# @admin.register(AboutUs)
class AboutUsAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        SectionInline,
        Section2Inline,
        Section3Inline,
        Section4Inline,
        Section5Inline,
        Section6Inline,
    ]
    filter_vertical = ('advantages',)

admin.site.register(AboutUs, AboutUsAdmin)

# Админка для управления заявками
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)
    ordering = ['-created_at']


# Отдельные админки для вложенных моделей
@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title',)

@admin.register(Gramota)
class GramotaAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title',)

@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title',)

@admin.register(Sertificat)
class SertificatAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title',)
