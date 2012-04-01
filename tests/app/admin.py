from django.contrib import admin
from app.models import Model


class ModelAdmin(admin.ModelAdmin):
    list_filter = ['boolean', 'date']
    list_display = ['char', 'integer', 'email', 'date']
    list_per_page = 2
    fieldsets = (
        (None, {
            'fields': ('char', 'decimal', 'float', 'integer', 'email', 'ip', 'text'),
            'description': 'Common string and digital fields'
        }),
        ('Boolean', {
            'classes': ('collapse',),
            'fields': ('boolean', 'null_boolean'),
            'description': 'Boolean fields'
        }),
        ('Dates', {
            'fields': ('date', 'time', 'datetime'),
        }),
        ('Files', {
            'fields': ('file', 'file_path', 'image'),
        }),
    )
    readonly_fields = ('decimal',)


admin.site.register(Model, ModelAdmin)
