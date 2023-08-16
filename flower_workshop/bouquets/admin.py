from django.contrib import admin

from .models import Flower, Event, BouquetFlower, Bouquet


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


class BouquetFlowerInline(admin.TabularInline):
    model = BouquetFlower
    extra = 0


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        'name',
        'price',
        'description',
    ]
    list_filter = [
        'events',
        'flowers',
    ]
    inlines = [
        BouquetFlowerInline,
    ]
