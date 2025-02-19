from django import forms
from accounts.models import CustomUser
from .models import CustomUser, Scambio
from dbPokemon.models import Espansione, Pokemon

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

class ScambioForm(forms.ModelForm):
    class Meta:
        model = Scambio
        fields = ["tipo", "espansione", "pokemon"]

    tipo = forms.ChoiceField(choices=Scambio.SCELTE_TIPO, widget=forms.RadioSelect)
    espansione = forms.ModelChoiceField(queryset=Espansione.objects.all(), empty_label="Seleziona un'espansione")
    pokemon = forms.ModelChoiceField(queryset=Pokemon.objects.none(), empty_label="Seleziona un Pokémon")

    def __init__(self, *args, **kwargs):
        super(ScambioForm, self).__init__(*args, **kwargs)
        if "espansione" in self.data:
            try:
                espansione_id = int(self.data.get("espansione"))
                self.fields["pokemon"].queryset = Pokemon.objects.filter(espansione_id=espansione_id)
            except (ValueError, TypeError):
                self.fields["pokemon"].queryset = Pokemon.objects.none()
        else:
            self.fields["pokemon"].queryset = Pokemon.objects.none()

