from django.contrib.auth.models import AbstractUser
from django.db import models


class User2(AbstractUser):
    on_vacation = models.BooleanField('в отпуске', default=False, db_index=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return '{0} - {1}. Email: {2}'.format(self.pk, self.first_name, self.email)
