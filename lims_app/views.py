from django.shortcuts import render
from django.contrib import admin
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect


def home(request):
    return render(request, "index.html", context={})

