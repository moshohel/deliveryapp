
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from core .models import User, Parcel, Divisions, Districts
from django.core import serializers
from .forms import ParcelForm, UserForm
from django.shortcuts import render, redirect
from utilities .user_permission import admin_user, merchant_user
from utilities .invoice import invoice
from utilities .parcel_price import Parcel_price


# Create Admin & Merchant User by Admin


@login_required
@user_passes_test(admin_user)
def createUser(request):
    msg = ""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            user_type = form.cleaned_data["user_type"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data["last_name"]
            photo = form.cleaned_data["photo"]

            User.objects.create_user(
                username=username,
                user_type=user_type,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                photo=photo
            )
            msg = "User Added Successefully"
            form = UserForm()
        else:
            error = "Something went wrong"
    else:
        form = UserForm()

    context = {
        "user_type": request.session.get("user_type"),
        'form': form,
        'message': msg
    }

    return render(request, 'create_user.html', context)


# Create Parcel and Save to Parcel Table


@login_required
@user_passes_test(admin_user)
def create_parcel(request):
    # Query for all Merchant
    merchants = User.objects.raw(
        """ SELECT * FROM user WHERE user_type = 'merchant_user' """)

    msg = ""

    if request.method == 'POST':
        form = ParcelForm(request.POST, request.FILES)
        if form.is_valid():
            parcel = Parcel()
            merchant = request.POST.get("merchant")
            parcel.merchant = User.objects.get(pk=merchant)
            parcel.product_type = form.cleaned_data["product_type"]
            parcel.weight = form.cleaned_data["weight"]
            parcel.district = form.cleaned_data.get("district")
            parcel.division = form.cleaned_data["division"]
            weight = float(request.POST['weight'])
            parcel.weight = weight
            data = request.POST['district']
            # Creating Parcel_price Class object
            parObj = Parcel_price(data, weight)
            price, return_charge = parObj.price()
            # Assigning price, return_charge value to parcel object
            parcel.return_charge = return_charge
            parcel.price = price
            parcel.address = form.cleaned_data["address"]
            # invoice Funcion call
            invoice_no = invoice()
            parcel.invoice_no = invoice_no
            parcel.save()
            msg = "Data entry User Added Successefully"
            context = {
                'message': msg,
            }
            return redirect("/")

        else:
            msg = "Something went wrong"

    context = {
        "user": request.session.get("user"),
        "merchants": merchants,
        'message': msg,
        "form": ParcelForm()
    }

    return render(request, "create_parcel.html", context)


# All Parcels


@login_required
@user_passes_test(admin_user)
def parcel_list(request):
    parcels = Parcel.objects.raw(""" SELECT parcel.id, parcel.invoice_no, parcel.product_type,
    parcel.weight, parcel.address, parcel.return_charge, parcel.price, division.name AS divi_name,
    district.name AS dist_name, user.photo, user.first_name AS merchant_first_name,
    user.last_name AS merchant_last_name FROM parcel parcel,
    divisions division, districts district, user user  WHERE parcel.division_id
    = division.id AND parcel.district_id = district.id AND parcel.merchant_id =
    user.id ORDER BY id DESC """)
    context = {
        "parcels": parcels
    }

    return render(request, "parcel_list.html", context)


# Parcel list for Merchant User


@login_required
@user_passes_test(merchant_user)
def merchant_parcel_list(request):
    parcels = Parcel.objects.raw(""" SELECT parcel.id, parcel.invoice_no, parcel.product_type, parcel.weight, parcel.address,
    parcel.price, parcel.return_charge, division.name AS divi_name, district.name AS dist_name FROM parcel parcel, divisions division,
    districts district WHERE parcel.division_id = division.id AND parcel.district_id = district.id
    AND parcel.merchant_id ='""" + str(request.session["user_id"]) + """' ORDER BY id DESC """)
    context = {
        "parcels": parcels
    }
    return render(request, "templates\merchant\parcel_list.html", context)


# Return Districts respect to Division


def districts_api(request, divi_id):
    query = "Select * from districts WHERE division_id =%s" % (divi_id)
    data = serializers.serialize('json', Districts.objects.raw(query))

    return HttpResponse(data)
