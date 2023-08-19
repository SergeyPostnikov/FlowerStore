from django.contrib import admin

from orders.models import Order

from bouquets.models import Bouquet

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...