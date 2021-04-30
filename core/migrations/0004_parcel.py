# Generated by Django 3.0.7 on 2021-04-29 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210429_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('F', 'Fragile'), ('L', 'Liquid')], max_length=2)),
                ('weight_in_gram', models.IntegerField(default=500)),
                ('address', models.CharField(max_length=200)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Districts')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Divisions')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Merchant')),
            ],
        ),
    ]
