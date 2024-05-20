from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportModelAdmin

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("full_name",)

    list_display = ('id', 'full_name')  # Listga qo'shish
    list_filter = ('full_name',)  # Filtrlash
