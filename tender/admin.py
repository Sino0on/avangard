from django.contrib import admin
from .models import Tender, MoreInfo, TenderApplication, Vacancies, VacanciApplication, Contacts, Requirement


class ContactInline(admin.StackedInline):
    model = Contacts
    extra = 1
    verbose_name = "Контакты"
    verbose_name_plural = "Контакты"


class RequerInline(admin.StackedInline):
    model = Requirement
    extra = 1
    verbose_name = "Требование"
    verbose_name_plural = "Требование"


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "mini_description")
    inlines = [ContactInline, RequerInline]

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