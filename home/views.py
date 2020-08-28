from django.shortcuts import render , HttpResponse , redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User

def home(request):
    return render(request , "home/home.html")

def about(request):
    messages.success(request, 'this is about')
    return render(request , "home/about.html")

def contact(request):
    messages.error(request, 'welcome to contact')
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        print(name, email,phone, content)
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request , "please fill the form properly.")
        else:
            contact= Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"your form has been submitted successfully.")
    return render(request , "home/contact.html")