# Generated by Django 4.1.2 on 2023-02-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=13, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='order',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=13, null=True, verbose_name='Longitude'),
        ),
    ]
