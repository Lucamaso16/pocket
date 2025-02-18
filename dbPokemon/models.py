from django.db import models

class Rarita(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    isScambiAttivi = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Rarità"
        verbose_name_plural = "Rarità"

    def __str__(self):
        return self.nome

class Espansione(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    isScambiAttivi = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Espansione"
        verbose_name_plural = "Espansioni"

    def __str__(self):
        return self.nome
    
class Pokemon(models.Model):
    espansione = models.ForeignKey(Espansione, on_delete=models.CASCADE, related_name="pokemon")
    pokedex = models.IntegerField()
    nome = models.CharField(max_length=100)
    rarita = models.ForeignKey(Rarita, on_delete=models.CASCADE)
    isScambiabile = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pokémon"
        verbose_name_plural = "Pokémon"

    def __str__(self):
        return f"{self.nome} - {self.rarita.nome} ({self.espansione.nome})"

    def save(self, *args, **kwargs):
        if self.espansione.isScambiAttivi and self.rarita.isScambiAttivi:
            self.isScambiabile = True
        super().save(*args, **kwargs)
    
# class TipoScambio(models.Model):
#     CERCO = 0
#     OFFRO = 1
#     TIPO_SCELTA = [
#         (CERCO, "Cerco"),
#         (OFFRO, "Offro")
#     ]

#     utente = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="scambi")
#     pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
#     tipo = models.IntegerField(choices=TIPO_SCELTA)

#     def __str__(self):
#         return f"{self.utente.username} {'cerca' if self.tipo == 0 else 'offre'} {self.pokemon.nome}"
