# from django.contrib import admin
# from .models import Service
# from import_export.admin import ImportExportModelAdmin
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     search_fields = ('AboutOurCarService',)
#

from django.contrib import admin
from .models import Service
from import_export.admin import ImportExportModelAdmin

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('AboutOurCarService',)  # Qidirish imkoniyatlari

    # Import/export sozlashlari
    list_display = ('id', 'AboutOurCarService')  # Listga qo'shish
    list_filter = ('AboutOurCarService',)  # Filtrlash
    fieldsets = (
        (None, {
            'fields': ('AboutOurCarService',)
        }),
    )
