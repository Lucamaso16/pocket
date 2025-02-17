from django.contrib import admin
from .models import Espansione, Pokemon, Rarita

class RaritaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'isScambiAttivi')
    list_filter = ('isScambiAttivi',)
    search_fields = ('nome',)

class EspansioneAdmin(admin.ModelAdmin):
    list_display = ('nome', 'isScambiAttivi')
    list_filter = ('isScambiAttivi',)
    search_fields = ('nome',)

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rarita', 'espansione', 'isScambiabile')
    search_fields = ('nome',)
    list_filter = ('isScambiabile',)

admin.site.register(Rarita, RaritaAdmin)
admin.site.register(Espansione, EspansioneAdmin)
admin.site.register(Pokemon, PokemonAdmin)

