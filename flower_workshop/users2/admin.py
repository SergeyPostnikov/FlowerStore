from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users2.models import User2


@admin.register(User2)
class User2Admin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'on_vacation',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'on_vacation',
        'is_superuser',
        'is_active',
        'is_staff',
    )
    search_fields = (
        'email',
        'username',
        'first_name',
    )
