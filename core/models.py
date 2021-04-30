from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import utils

PERCEL_PRODUCT_TYPE = (
    ('F', 'Fragile'),
    ('L', 'Liquid')
)

class Merchant(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100, unique=True)
    # user_type = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='photo/%Y%m/%d/', blank=True)
    created_at = models.DateTimeField(default=utils.timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # def as_json(self):
    #     return dict(
    #         username = self.username,
    #         # user_type = self.user_type,
    #         photo = self.photo,
    #         created_at = self.created_at,
    #         updated_at = self.updated_at
    #     )
    class Meta:
        db_table = "merchant"

class Divisions(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Districts(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Parcel(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_type = models.CharField(choices=PERCEL_PRODUCT_TYPE, max_length=2)
    weight_in_gram = models.IntegerField(default=500)
    division = models.ForeignKey(Divisions, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(Districts, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.merchant