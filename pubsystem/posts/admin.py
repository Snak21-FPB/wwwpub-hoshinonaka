from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models

class BureauAdmin(ModelAdmin):
    list_display = ("name", "created_by", "created_at", "updated_by", "updated_at")

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(models.Bureau,BureauAdmin)
