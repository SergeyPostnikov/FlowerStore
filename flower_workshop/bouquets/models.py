from django.db import models


class Event(models.Model):
    name = models.CharField(
        'Название события',
        max_length=100,
        blank=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(
        'Цветок',
        max_length=100,
        blank=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Виды цветов'

    def __str__(self):
        return self.name
