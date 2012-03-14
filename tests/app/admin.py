from django.contrib import admin
from app.models import Model


class ModelAdmin(admin.ModelAdmin):
    list_filter = ['boolean', 'date']


admin.site.register(Model, ModelAdmin)
