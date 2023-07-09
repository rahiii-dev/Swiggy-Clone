# Generated by Django 4.1.2 on 2023-02-27 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_specials'),
        ('cart', '0008_alter_cartmodel_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurant.restaurant'),
        ),
    ]
