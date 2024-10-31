from django.shortcuts import render
from django.contrib import admin
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect


def home(request):
    return render(request, "index.html", context={})

def contact(request):
    return render(request, "contact.html")

def save_student(request):
    #get student name entered by user
    student_name = request.POST['student_name']
    return render(request, "welcome.html",context={'student_name':student_name})
    #context to send data to welcome.html file