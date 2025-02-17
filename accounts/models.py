from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model

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
    
# class OggettoScambio(models.Model):
#     utente = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="oggetti_scambio")
#     pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
#     tipo = models.IntegerField(choices=TipoScambio.TIPO_SCELTA)

#     def __str__(self):
#         return f"{self.utente.username} {'cerca' if self.tipo == 0 else 'offre'} {self.pokemon.nome}"