from django.contrib import admin
from app.models import Model


class ModelAdmin(admin.ModelAdmin):
    list_filter = ['boolean', 'date']
    list_display = ['char', 'integer', 'email', 'date']
    list_per_page = 2


admin.site.register(Model, ModelAdmin)
