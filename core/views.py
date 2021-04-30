from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View


def index(request):
    return HttpResponse("Hello, world. You're at the core index.")

def home_page(request):
    return render(request, "home.html")