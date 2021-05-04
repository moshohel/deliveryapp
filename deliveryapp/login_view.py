from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from core.models import User
from utilities.user_types_value import user_types


def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if request.POST['username'] != '' and request.POST['password'] != '':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                userType = user.user_type
                request.session["user_id"] = user.id
                request.session["user_type"] = userType
                request.session["name"] = user.first_name + \
                    " " + user.last_name
                is_staff = user.is_staff
                if (userType == user_types().admin):
                    return redirect('/admin_user/createUser/')

                elif(userType == user_types().merchant):
                    return redirect('/merchant/parcel_list')

                elif(is_staff):
                    return redirect('/admin')

            else:
                context = {
                    'errorMsg': "username or password is invalid"
                }
                return render(request, 'login.html', context)
        else:
            context = {
                'errorMsg': "username or pass can not be empty"
            }
            return render(request, 'login.html', context)
    else:
        context = {
            'errorMsg': ""
        }
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
