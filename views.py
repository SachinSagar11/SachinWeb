from django.shortcuts import render, HttpResponse
from datetime import datetime
from SachinApp.models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
    
   
    #return HttpResponse('This is First Apps HomePage')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This is about my First Apps HomePage')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('This is about my services povided here')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Message was sent successfully!')
    return render(request, 'contact.html')
    #return HttpResponse('You can call us on : 98545xxxxx also write us on shopyjuice@gmail.com')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    return redirect("/login")