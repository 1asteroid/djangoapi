# Generated by Django 5.0.3 on 2024-05-16 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryaddress',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.order'),
        ),
    ]