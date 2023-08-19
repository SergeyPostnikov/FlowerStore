from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

from bouquets.models import Bouquet


# Create your models here.
class StatusOrder(models.TextChoices):
    unprocessed = 'Необработанный заказ', 'Необработанный заказ'
    in_work = 'Собирается флористом', 'Собирается флористом'
    delivery = 'Передан курьеру', 'Передан курьеру'
    completed = 'Заказ завершён', 'Заказ завершён'


class Order(TimeStampedModel):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='client_orders',
        verbose_name='Клиент')
    bouquet = models.ForeignKey(
        Bouquet,
        on_delete=models.PROTECT,
        verbose_name='Букет'
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Сумма'
    )
    from_delivery_time = models.DateTimeField(
        verbose_name='Интервал доставки ОТ'
    )
    to_delivery_time = models.DateTimeField(
        verbose_name='Интервал доставки ДО'
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес'
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона'
    )
    status = models.CharField(
        max_length=21,
        verbose_name='Статус заказа',
        choices=StatusOrder.choices,
        default=StatusOrder.unprocessed,
        db_index=True)

    courier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courier_orders',
        verbose_name='Курьер'
    )
    florist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='florist_orders',
        verbose_name='Флорист')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.status

