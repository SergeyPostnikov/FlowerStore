from decimal import Decimal

from django.db import models


class Event(models.Model):
    name = models.CharField('Название события', max_length=100, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField('Цветок', max_length=100, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Виды цветов'

    def __str__(self):
        return self.name


class BouquetFlower(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.PROTECT, verbose_name='Цветов')
    quantity = models.PositiveSmallIntegerField('Количество')
    bouquet = models.ForeignKey(
        'bouquets.Bouquet',
        on_delete=models.PROTECT,
        verbose_name='букет',
        related_name='flowers',
    )

    class Meta:
        verbose_name = 'Цветок в букете'
        verbose_name_plural = 'Цветы в букете'

    def __str__(self):
        return '{0} - {1}'.format(self.flower, self.quantity)


class Bouquet(models.Model):
    name = models.CharField('Название', max_length=100, blank=True, db_index=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0'))
    image = models.ImageField(upload_to='bouquets_images', blank=True, null=True)
    description = models.TextField('Описание', blank=True)
    events = models.ManyToManyField(Event, verbose_name='События')
    recommended = models.BooleanField('В рекомендованных', default=False, db_index=True)

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.price)
