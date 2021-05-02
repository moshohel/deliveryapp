from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_parcel', views.create_parcel, name='create_parcel'),
    path('list', views.parcel_list, name='parcel_list'),
]