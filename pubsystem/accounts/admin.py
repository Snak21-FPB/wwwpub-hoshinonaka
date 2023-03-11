from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account

class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields":("email","username","password")}),
        (("権限"),{"fields":("is_active","is_staff")}),
        (("ログイン記録"),{"fields":("date_joined",)})
    )

admin.site.register(Account, AccountAdmin)
