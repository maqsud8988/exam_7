from django.contrib import admin
from .models import Furnitures
from import_export.admin import ImportExportModelAdmin

@admin.register(Furnitures)
class FurnituresAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("WhatWeDo",)


    list_display = ('id', 'WhatWeDo')  # Listga qo'shish
    list_filter = ('WhatWeDo',)  # Filtrlash





