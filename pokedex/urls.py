from django.urls import path

from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("entrenador/<int:id>/", views.trainer, name="trainer"),
    path("entrenador/add/", views.add_trainer, name="add_trainer"),
]