# Generated by Django 4.2.4 on 2023-08-18 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bouquets', '0003_bouquet_recommended'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+79243455454', max_length=128, region=None, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='bouquet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bouquets.bouquet', verbose_name='Букет'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_orders', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courier_orders', to=settings.AUTH_USER_MODEL, verbose_name='Курьер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='florist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='florist_orders', to=settings.AUTH_USER_MODEL, verbose_name='Флорист'),
        ),
        migrations.AlterField(
            model_name='order',
            name='from_delivery_time',
            field=models.DateTimeField(verbose_name='Интервал доставки ОТ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Необработанный заказ', 'Необработанный заказ'), ('Собирается флористом', 'Собирается флористом'), ('Передан курьеру', 'Передан курьеру'), ('Заказ завершён', 'Заказ завершён')], db_index=True, default='Необработанный заказ', max_length=21, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='to_delivery_time',
            field=models.DateTimeField(verbose_name='Интервал доставки ДО'),
        ),
    ]
