from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.validators import PhoneNumber

class Consultation(models.Model):
    class Statuses(models.TextChoices):
        NOT_PROCESSED = 'NP', 'Не обработана'
        DENIED = 'DN', 'Отказ'
        ORDER = 'OR', 'Сделан заказ'

    florist = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Флорист'
    )
    name = models.CharField(
        'Имя',
        max_length=100,
        db_index=True,
        validators=[MinLengthValidator(3)],
    )
    phone = PhoneNumberField('Телефон', db_index=True)
    status = models.CharField(
        'Статус', max_length=2, choices=Statuses.choices, default=Statuses.NOT_PROCESSED, db_index=True
    )

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name, self.phone, self.status)
