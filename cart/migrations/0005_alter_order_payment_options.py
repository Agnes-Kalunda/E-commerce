# Generated by Django 3.2 on 2022-07-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_order_payment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_options',
            field=models.BooleanField(choices=[('M-pesa', 'M-pesa'), ('Paypal', 'Paypal'), ('stripe', 'stripe')], default=False),
        ),
    ]