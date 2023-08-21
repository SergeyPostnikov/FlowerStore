from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField

from bouquets.models import Bouquet


# Create your models here.
class StatusOrder(models.TextChoices):
    unprocessed = 'UP', 'Необработанный заказ',
    in_work = 'IW', 'Собирается флористом'
    delivery = 'DL', 'Передан курьеру'
    completed = 'CP', 'Заказ завершён'


class IntervalOrder(models.TextChoices):
    first = 'FRS', 'Как можно скорее'
    two = 'TW', 'с 10:00 до 12:00'
    three = 'TH', 'с 12:00 до 14:00'
    four = 'FR', 'с 14:00 до 16:00'
    five = 'FV', 'с 16:00 до 18:00'
    six = 'SX', 'с 18:00 до 20:00'


class Order(TimeStampedModel):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='client_orders',
        verbose_name='Клиент',
    )
    client_name = models.CharField(
        max_length=80,
        verbose_name='Имя клиента',
        db_index=True,
    )
    bouquet = models.ForeignKey(
        Bouquet,
        on_delete=models.PROTECT,
        verbose_name='Букет'
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Сумма',
    )
    delivery_time = models.CharField(
        max_length=17,
        verbose_name='Интервал доставки',
        choices=IntervalOrder.choices,
        default=IntervalOrder.first,
        db_index=True
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес',
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона',
    )
    status = models.CharField(
        max_length=2,
        verbose_name='Статус заказа',
        choices=StatusOrder.choices,
        default=StatusOrder.unprocessed,
        db_index=True,
    )
    courier = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courier_orders',
        verbose_name='Курьер',
    )
    florist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='florist_orders',
        verbose_name='Флорист',
    )
    paid = models.BooleanField(
        'Оплачен',
        default=False,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)
