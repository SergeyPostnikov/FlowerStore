from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class CounsultationAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'phone',
    ]
    list_display = [
        'phone',
        'name',
        'status',
        'florist',
    ]
    list_filter = [
        'status',
        'florist',
    ]
    raw_id_fields = [
        'florist',
    ]
