from .views import create_order, order_step, my_order

from django.urls import path

urlpatterns = [
    path('', create_order, name='order'),
    path('step/', order_step, name='order-step'),
    path('my-order/<int:pk>/', my_order, name='my_order'),
]
