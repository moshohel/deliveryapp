# Generated by Django 3.2 on 2021-05-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_parcel_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='price',
            field=models.FloatField(default=60, max_length=5),
        ),
    ]