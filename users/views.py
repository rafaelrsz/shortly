from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as logout_django
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Bem-vindo, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('login')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else: 
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "Esse nome de usuário já está em uso.")
            return redirect('register') 

        if User.objects.filter(email=email).exists():
            messages.error(request, "Esse e-mail já está em uso.")
            return redirect('register')

        User.objects.create_user(username=usuario, email=email, password=senha)
        messages.success(request, f"Usuário {usuario} cadastrado com sucesso!")
        return redirect('login')

@login_required(login_url='login')
def logout(request):
    logout_django(request)
    return redirect('login')