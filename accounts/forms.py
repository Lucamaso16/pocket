from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import CustomUser
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    codice_amico = forms.CharField(
        max_length=16, min_length=16,
        required=True, label="Codice Amico",
        widget=forms.TextInput(attrs={'placeholder': 'Inserisci codice amico'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Inserisci password'}),
        label="Password"
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Conferma password'}),
        label="Conferma passowrd"
    )

    class Meta:
        model = CustomUser
        fields = ["username", "codice_amico", "password", "password_confirm"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Le password non coincidono!")

        codice_amico = cleaned_data.get("codice_amico")
        if codice_amico and (not codice_amico.isdigit() or len(codice_amico) != 16):
            self.add_error("codice_amico", "Il codice amico deve contenere esattamente 16 cifre")

        return cleaned_data

