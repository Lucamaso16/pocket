from django.urls import path
from .views import register, CustomLoginView, user_logout, profile_view, get_pokemon_ajax, elimina_scambio

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path("ajax/get_pokemon/", get_pokemon_ajax, name="get_pokemon_ajax"),
    path('elimina_scambio/<int:scambio_id>/', elimina_scambio, name='elimina_scambio'),
]
