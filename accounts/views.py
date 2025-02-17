from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm
from accounts.models import CustomUser

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            codice_amico = form.cleaned_data["codice_amico"]
            password = form.cleaned_data["password"]

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Questo nome utente è gia registrato")
            else:
                user = CustomUser.objects.create_user(username=username, codice_amico=codice_amico, password=password)
                user.codice_amico = codice_amico
                user.save()
                messages.success(request, "Registrazione completata!")
                return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def user_logout(request):
    logout(request)
    return redirect('/')

def profile_view(request):
    return render(request, 'accounts/profile.html')