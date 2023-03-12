from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models

class BureauAdmin(ModelAdmin):
    list_display = ("name", "created_by", "created_at", "updated_by", "updated_at")

admin.site.register(models.Bureau,BureauAdmin)
