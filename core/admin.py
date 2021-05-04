from django.contrib import admin
from .models import User, Parcel, Divisions, Districts

# Register models for admin.
admin.site.register(User)
# admin.site.register(Merchant)
admin.site.register(Parcel)
admin.site.register(Divisions)
admin.site.register(Districts)
