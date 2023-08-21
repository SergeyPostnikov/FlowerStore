from .views import create_order, order_step

from django.urls import path

urlpatterns = [
    path('', create_order, name='order'),
    path('step/', order_step, name='order-step'),
]
