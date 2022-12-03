from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import UserForm


def register(request):
    form=UserForm()
    if request.method=='POST':
        #type=request.POST.get('type')
        print(request.POST)

        form=UserForm(data=request.POST)

        if form.is_valid():
            #form.type=type

            form.save()
            messages.success(request,'Votre compte a été créé')
            return redirect('login')
        else:
            messages.error(request,form.errors)
    return  render(request,"accounts/register.html",context={"form":form})

@login_required(login_url='login')
def deconnection(request):
    logout(request)
    return redirect("home")


def connection(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,"Bienvenue")
            return redirect("home")

        else:
            messages.error(request,"Erreur d'authentification")
    return render(request,"accounts/login.html")