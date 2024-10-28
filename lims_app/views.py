from django.shortcuts import render
from django.contrib import admin
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect


def home(request):
    return HttpResponse('hello world')

def shopping(request):
    return H