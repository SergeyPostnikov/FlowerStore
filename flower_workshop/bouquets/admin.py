from django.contrib import admin

from .models import Flower, Event


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]
