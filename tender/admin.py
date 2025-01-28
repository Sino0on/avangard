from django.contrib import admin
from .models import Tender, MoreInfo, TenderApplication, Vacancies, VacanciApplication


class MoreInfoInline(admin.StackedInline):
    model = MoreInfo
    extra = 1
    verbose_name = "Дополнительная информация"
    verbose_name_plural = "Дополнительная информация"


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "mini_description")
    inlines = [MoreInfoInline]

@admin.register(VacanciApplication)
class VacanciAdmin(admin.ModelAdmin):
    list_display = ("fullname", "created_at")
    search_fields = ("fullname", "created_at")



@admin.register(TenderApplication)
class TenderApplicationAdmin(admin.ModelAdmin):
    list_display = ("company_name", "tender", "created_at")
    search_fields = ("company_name", "theme", "email")
    list_filter = ("created_at", "tender")


admin.site.register(Vacancies)