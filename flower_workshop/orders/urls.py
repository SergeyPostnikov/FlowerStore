from .views import order_view, order_step

from django.urls import path

urlpatterns = [
    path('', order_view, name='order'),
    path('step/', order_step, name='order-step'),
]
