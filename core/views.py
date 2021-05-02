from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required, user_passes_test
from core .models import User, Parcel, Divisions, Districts, Merchant
from django.http import JsonResponse
import json
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the core index.")

def home_page(request):
    return render(request, "home.html")

# Create Parcel and Save to Parcel Table
@login_required
def create_parcel(request):
    if request.method == 'POST':
        parcel = Parcel()
        parcel.product_type = request.POST['product_type']
        parcel.weight_in_gram = request.POST['weight_in_gram']
        parcel.division_id = request.POST.get('division')
        parcel.district_id = request.POST.get('district')
        parcel.address = request.POST['address']
        parcel.merchant_id = request.POST.get('merchant')
        parcel.save()

    merchants = Merchant.objects.raw("Select * from merchant")
    divisions = Divisions.objects.raw("Select * from core_divisions")
    districts = Districts.objects.raw("Select * from core_districts")
    print(merchants)
    print(divisions)
    print(districts)
    context = {
        "user": request.session.get("user"),
        "merchants": merchants,
        "districts": districts,
        "divisions": divisions,
    }

    return render(request, "create_parcel.html", context)

def parcel_list(request):
    parcels = Parcel.objects.all()
    context = {
        "parcels": parcels
    }

    return render(request, "parcel_list.html", context)

# Return Districts respect to Division
def districts_api(request, divi_id):
    query = "Select * from core_districts WHERE division_id =%s"%(divi_id)
    data = serializers.serialize('json', Districts.objects.raw(query))

    return HttpResponse(data)
