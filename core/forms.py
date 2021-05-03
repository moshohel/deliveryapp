from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['merchant', 'product_type', 'weight', 'division', 'district', 'address']
        # widgets = {
        #     'product_type': forms.Select(attrs={'class': 'custom-select md-form'}),
        # }
# print (ParcelForm().as_p())
