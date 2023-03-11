from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account

class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields":("email","username","password")}),
        (("権限"),{"fields":("is_active","is_staff")}),
        (("ログイン記録"),{"fields":("date_joined","last_login")})
    )

    add_fieldsets = (
        (None, {"classes":("wide",),"fields":("email","username","password1","password2")}),
    )

    list_display = ("username", "email", "is_active", "is_staff", "last_login")
    list_filter = ("is_active", "is_staff")
    search_fields = ("username","email")
    ordering = ("date_joined",)

admin.site.register(Account, AccountAdmin)

