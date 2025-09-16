from django.urls import path
from . import views

urlpatterns = [
    path('pokemons/', views.mostrar_pokemon, name='lista_pokemon'),
]