from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, codice_amico, password=None):
        if not username:
            raise ValueError("Il campo 'username' è obbligatorio")
        if not codice_amico:
            raise ValueError("Il campo 'codice amico' è obbligatorio")

        user = self.model(username=username, codice_amico=codice_amico)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, codice_amico, password):
        user = self.create_user(username, codice_amico, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    codice_amico = models.CharField(max_length=16, unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

