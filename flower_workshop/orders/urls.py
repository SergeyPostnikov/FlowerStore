from .views import order, order_step

from django.urls import path

urlpatterns = [
    path('', order, name='order'),
    path('step/', order_step, name='order-step'),
]
