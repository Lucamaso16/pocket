from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, ScambioForm
from .models import Scambio
from accounts.models import CustomUser
from django.http import JsonResponse
from dbPokemon.models import Pokemon

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

@login_required
def profile_view(request, user_id=None):
    if user_id:
        user = get_object_or_404(CustomUser, id=user_id)
        is_own_profile = user == request.user
    else:
        user = request.user
        is_own_profile = True

    scambi_utente = Scambio.objects.filter(utente=user)
    form = ScambioForm(request.POST or None) if is_own_profile else None

    if request.method == "POST" and form and form.is_valid():
        scambio = form.save(commit=False)
        scambio.utente = request.user
        scambio.save()

        # Modifica qui per includere il user_id nel redirect
        return redirect('profile', user_id=user.id)

    return render(request, "accounts/profile.html", {
        "user": user,
        "is_own_profile": is_own_profile,
        "form": form,
        "scambi": scambi_utente
    })


def get_pokemon_ajax(request):
    espansione_id = request.GET.get("espansione")
    
    if espansione_id:
        pokemon_list = Pokemon.objects.filter(espansione_id=espansione_id).values("id", "nome")
        return JsonResponse({"pokemon": list(pokemon_list)})
    
    return JsonResponse({"pokemon": []})

@login_required
def elimina_scambio(request, scambio_id):
    scambio = get_object_or_404(Scambio, id=scambio_id)

    if scambio.utente == request.user:
        scambio.delete()
        return redirect('profile', user_id=request.user.id)

    return redirect('profile', user_id=request.user.id)