# Generated by Django 5.0.4 on 2024-05-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_alter_city_options_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='acceptance',
            field=models.BooleanField(default=False),
        ),
    ]