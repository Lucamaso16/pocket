from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creiamo un superuser senza richiedere il campo codice_amico.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    codice_amico = models.CharField(max_length=16, blank=True, null=True)

    objects = CustomUserManager()

class Scambio(models.Model):
    CERCO = 0
    OFFRO = 1
    SCELTE_TIPO = [
        (CERCO, "Cerco"),
        (OFFRO, "Offro"),
    ]

    utente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Scambi")
    tipo = models.IntegerField(choices=SCELTE_TIPO)
    espansione = models.ForeignKey("dbPokemon.Espansione", on_delete=models.CASCADE)
    pokemon = models.ForeignKey("dbPokemon.Pokemon", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Scambio"
        verbose_name_plural = "Scambi"

    def __str__(self):
        return f"{self.utente.username} - {'Cerco' if self.tipo == 0 else 'Offro'} {self.pokemon.nome}"