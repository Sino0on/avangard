from django.contrib import admin
from .models import *


class SectionInline(admin.StackedInline):
    model = Section1
    extra = 0


class MaterialsInline(admin.StackedInline):
    model = Materials
    extra = 1  # Количество пустых форм для добавления


class Section2Inline(admin.StackedInline):
    model = Section2
    inlines = [MaterialsInline]
    extra = 0

    # Убедитесь, что вы добавляете MaterialInline как часть админки
    def get_inline_instances(self, request, obj=None):
        inlines = super().get_inline_instances(request, obj)
        if obj:
            inlines.append(MaterialsInline(self.model, self.admin_site))
        return inlines


class Section3Inline(admin.StackedInline):
    model = Section3
    extra = 0


class GramotaInline(admin.StackedInline):
    model = Gramota
    extra = 1  # Количество пустых форм для добавления


class Section4Inline(admin.StackedInline):
    model = Section4
    inlines = [GramotaInline]
    extra = 0

    def get_inline_instances(self, request, obj=None):
        inlines = super().get_inline_instances(request, obj)
        if obj:
            inlines.append(GramotaInline(self.model, self.admin_site))
        return inlines


class LicenceInline(admin.StackedInline):
    model = Licence
    extra = 1  # Количество пустых форм для добавления


class Section5Inline(admin.StackedInline):
    model = Section5
    inlines = [LicenceInline]
    extra = 0

    def get_inline_instances(self, request, obj=None):
        inlines = super().get_inline_instances(request, obj)
        if obj:
            inlines.append(LicenceInline(self.model, self.admin_site))
        return inlines


class Section6Inline(admin.StackedInline):
    model = Section6
    extra = 0


class AboutUsAdmin(admin.ModelAdmin):
    inlines = [
        SectionInline,
        Section2Inline,
        Section3Inline,
        Section4Inline,
        Section5Inline,
        Section6Inline,
    ]
    filter_vertical = ('advantages',)


class SertificatInline(admin.StackedInline):
    model = Sertificat
    extra = 0


@admin.register(Section6)
class Section6Admin(admin.ModelAdmin):
    inlines = [
        SertificatInline,
    ]


class LicenceInline(admin.StackedInline):
    model = Licence
    extra = 0


@admin.register(Section5)
class Section5Admin(admin.ModelAdmin):
    inlines = [
        LicenceInline,
    ]


class GramotaInline(admin.StackedInline):
    model = Gramota
    extra = 0


@admin.register(Section4)
class Section4Admin(admin.ModelAdmin):
    inlines = [
        GramotaInline,
    ]


class MaterialsInline(admin.StackedInline):
    model = Materials
    extra = 0


@admin.register(Section2)
class Section2Admin(admin.ModelAdmin):
    inlines = [
        MaterialsInline,
    ]


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
