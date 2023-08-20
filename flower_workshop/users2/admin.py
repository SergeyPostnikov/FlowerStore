from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users2.models import User2


@admin.register(User2)
class User2Admin(UserAdmin):
    fieldsets = (
        ('Mobile Phone', {'fields': ('type',)}),
        *UserAdmin.fieldsets,
    )
    list_display = (
        'email',
        'first_name',
        'type',
        'on_vacation',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'type',
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
