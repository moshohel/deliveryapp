from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required, user_passes_test
from core .models import User, Parcel, Divisions, Districts
from django.http import JsonResponse
from django.core import serializers
from .forms import ParcelForm, UserForm
from django.shortcuts import render, redirect, reverse
from utilities .user_permission import admin_user, merchant_user


def index(request):
    return HttpResponse("Hello, world. You're at the core index.")


def home_page(request):
    return render(request, "home.html")

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
            UserForm().clean()
        else:
            error = "Something went wrong"
    else:
        form = UserForm()

    # UnitName = Police_unit.objects.raw("Select * from police_unit where police_range_id = '"+ str(request.session["police_range_id"])+"'")

    # rangeName = Police_range.objects.raw("Select * from police_range")

    context = {
        "user_type": request.session.get("user_type"),
        'form': form,
        'message': msg
    }

    return render(request, 'create_user.html', context)

# Create Parcel and Save to Parcel Table


@login_required
def create_parcel(request):
    msg = ""
    if request.method == 'POST':
        form = ParcelForm(request.POST, request.FILES)
        # print(request.POST)

        if form.is_valid():
            merchant = form.cleaned_data["merchant"]
            product_type = form.cleaned_data["product_type"]
            weight = form.cleaned_data["weight"]
            district = form.cleaned_data["district"]
            district = form.cleaned_data.get("district")
            division = form.cleaned_data["division"]
            print(request.POST)
            weight = float(request.POST['weight'])
            # print(type(weight))
            print(request.POST['weight'])
            price = 0
            # print(request.POST['division'])
            # print(request.user)
            # print(form.cleaned_data)
            print(type(district), district)
            # print(division)
            if request.POST['district'] == '47' and request.POST['division'] == '6':
                if weight < 2:
                    price = 60
                    print(f'division & district dhaka - ', {price})
                else:
                    price = ((weight-2)*10)+60
                    print(f'division & district dhaka - ', {price})
            elif request.POST['division'] == '6':
                if weight < 2:
                    price = 110
                    print(f'division dhaka - ', {price})
                else:
                    price = ((weight-2)*20)+110
                    print(f'division dhaka - ', {price})
            else:
                if weight < 2:
                    price = 130
                    print(f'outside - ', {price})
                else:
                    price = ((weight-2)*20)+130
                    print(f'outside - ', {price})

            address = form.cleaned_data["address"]
            Parcel.objects.create(
                merchant=merchant,
                product_type=product_type,
                weight=weight,
                division=division,
                district=district,
                address=address
            )
            # form.save()
            msg = "Data entry User Added Successefully"
            context = {
                'message': msg,
            }
            return redirect("/")

        else:
            msg = "Something went wrong"

    # if request.method == 'POST':
    #     parcel = Parcel()
    #     parcel.product_type = request.POST['product_type']
    #     parcel.weight = request.POST['weight']
    #     parcel.division_id = request.POST.get('division')
    #     parcel.district_id = request.POST.get('district')
    #     parcel.address = request.POST['address']
    #     parcel.merchant_id = request.POST.get('merchant')
    #     parcel.save()

    # merchants = Merchant.objects.raw("Select * from merchant")
    # divisions = Divisions.objects.raw("Select * from core_divisions")
    # districts = Districts.objects.raw("Select * from core_districts")

    context = {
        "user": request.session.get("user"),
        # "merchants": merchants,
        # "districts": districts,
        # "divisions": divisions,
        'message': msg,
        "form": ParcelForm()
    }

    return render(request, "create_parcel.html", context)


def parcel_list(request):
    # parcels = Parcel.objects.all()
    parcels1 = Parcel.objects.order_by('-id')
    parcels = Parcel.objects.raw(""" SELECT parcel.id, parcel.product_type,
    parcel.weight, parcel.address, division.name AS divi_name,
    district.name AS dist_name, merchant.name AS merchant_name FROM core_parcel parcel,
    core_divisions division, core_districts district, merchant merchant  WHERE parcel.division_id
    = division.id AND parcel.district_id = district.id AND parcel.merchant_id =
    merchant.id ORDER BY id DESC """)
    context = {
        "parcels": parcels
    }

    return render(request, "parcel_list.html", context)


def merchant_parcel_list(request):
    return render(request, "templates\merchant\parcel_list.html", context)

# Return Districts respect to Division


def districts_api(request, divi_id):
    query = "Select * from core_districts WHERE division_id =%s" % (divi_id)
    data = serializers.serialize('json', Districts.objects.raw(query))

    return HttpResponse(data)
