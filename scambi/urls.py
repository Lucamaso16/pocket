from django.urls import path
from .views import general, users_list

urlpatterns = [
    path('', general, name='general'),
    path('users/', users_list, name='users_list'),
]