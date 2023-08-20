from django.urls import path

from .views import card, catalog, quiz_delivery, quiz_payment, result

app_name = 'bouquets'

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('result/', result, name='result'),
    path('quiz/drlivery-step/', quiz_delivery, name='quiz_delivery_step'),
    path('quiz/payment-step/', quiz_payment, name='quiz_payment_step'),
    path('card/<int:pk>/', card, name='card'),
]
