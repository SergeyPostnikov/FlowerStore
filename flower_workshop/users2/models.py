from django.contrib.auth.models import AbstractUser
from django.db import models


class User2(AbstractUser):
    class Types(models.TextChoices):
        CLIENT = 'CL', 'Клиент'
        FLORIST = 'FL', 'Флорист'
        COURIER = 'CO', 'Курьер'
        MANAGER = 'MA', 'Менеджер'

    on_vacation = models.BooleanField('В отпуске', default=False, db_index=True)
    type = models.CharField('Тип', max_length=2, choices=Types.choices, default=Types.CLIENT, db_index=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return '{1} ({2})'.format(self.pk, self.first_name, self.email)
