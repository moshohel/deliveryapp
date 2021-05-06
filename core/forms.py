from django import forms
from .models import Parcel, User


class ParcelForm(forms.ModelForm):

    class Meta:
        model = Parcel
        fields = ['merchant', 'product_type', 'weight',
                  'division', 'district', 'address']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'user_type',
                  'photo', 'email', 'first_name', 'last_name']
