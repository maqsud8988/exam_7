from django.contrib import admin
from .models import Testimonial
from import_export.admin import ImportExportModelAdmin

@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ('id', 'name')  # Listga qo'shish
    list_filter = ('name',)  # Filtrlash
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )


