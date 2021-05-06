from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import utils

PERCEL_PRODUCT_TYPE = (
    ('Fragile', 'Fragile'),
    ('Liquid', 'Liquid')
)


USER_TYPE = (
    ('admin_user', 'admin_user'),
    ('merchant_user', 'merchant_user')
)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    user_type = models.CharField(
        choices=USER_TYPE, max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='photo/%Y%m/%d/', blank=True)
    created_at = models.DateTimeField(default=utils.timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"


class Divisions(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "divisions"


class Districts(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "districts"


class Parcel(models.Model):
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.CharField(choices=PERCEL_PRODUCT_TYPE, max_length=10)
    weight = models.FloatField(default=0.5)
    division = models.ForeignKey(Divisions, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(Districts, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)
    price = models.FloatField(default=60, max_length=5)
    return_charge = models.FloatField(default=0, max_length=5)
    invoice_no = models.CharField(
        max_length=500, null=True, blank=True)

    def __str__(self):
        return self.merchant

    class Meta:
        db_table = "parcel"
