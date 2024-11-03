from django.shortcuts import render
from django.contrib import admin
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect


def home(request):
    return render(request, "home.html", context={"current_tab":"home"})
def readers(request):
    return render(request, "readers.html", context={"current_tab":"readers"})

def returns(request):
    return render(request, "returns.html", context={"current_tab":"returns"})
def contact(request):
    return render(request, "contact.html", context={"current_tab":"contact"})

def save_student(request):
#Get student name and age entered by user
    if request.method == "POST":
        student_name =request.POST.get('student_name')
        student_age = request.POST.get('student_age')
# If student information is provided, pass it to the context
    if student_name and student_age:
            return render(request, "welcome.html", context={'student_name': student_name,
                                                            'student_age': student_age
                                                            })

    return redirect('home')


#context to send data to welcome.html file