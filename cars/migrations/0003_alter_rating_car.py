# Generated by Django 4.0 on 2021-12-17 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_make_car_car_make_rename_model_car_car_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='cars.car'),
        ),
    ]
