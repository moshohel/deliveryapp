# Generated by Django 3.2 on 2021-05-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='weight',
            field=models.FloatField(default=0.5),
        ),
    ]
