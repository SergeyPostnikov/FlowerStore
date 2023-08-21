from django.contrib import admin

from orders.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


class FloristListFilter(admin.SimpleListFilter):
    title = "Флорист"
    parameter_name = "florist"
    florists = User.objects.filter(type=User.Types.FLORIST)
    florists_name_list = list(florists.values_list('pk', 'first_name'))

    def lookups(self, request, model_admin):
        return self.florists_name_list

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(florist__pk=self.value())


class CourierListFilter(admin.SimpleListFilter):
    title = "Курьер"
    parameter_name = "courier"
    florists = User.objects.filter(type=User.Types.COURIER)
    florists_name_list = list(florists.values_list('pk', 'first_name'))

    def lookups(self, request, model_admin):
        return self.florists_name_list

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(florist__pk=self.value())


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'phone',
        'client_name',
        'status',
        'paid',
        'florist',
        'courier',
    ]
    list_filter = [
        CourierListFilter,
        FloristListFilter,
        'status',
        'paid',
    ]
    raw_id_fields = [
        'florist',
        'courier',
        'client',
    ]



