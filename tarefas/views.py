from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def home(request):
    return render (
        request,"template/home.html" 
    )

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        error = "Usuário ou senha inválidos."
        return render(request, "template/login.html", 
        {"error":error},

        )
        
    return render (request,"template/login.html")

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    
    else:
        form = RegisterForm()

    return render (request,"template/register.html", 
    {"form": form},
        
    )
    

def password_reset(request):
    return render(
        request,"template/password_reset.html"
    )

