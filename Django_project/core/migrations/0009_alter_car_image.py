# Generated by Django 5.1.6 on 2025-03-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='car_images/default.png', upload_to='car_images/'),
        ),
    ]
