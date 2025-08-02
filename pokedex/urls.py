from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.custom_logout, name="logout"),
    
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("pokemon/edit/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemon/delete/<int:id>/", views.delete_pokemon, name="delete_pokemon"),
    
    path("entrenador/<int:id>/", views.trainer, name="trainer"),
    path("entrenador/add/", views.add_trainer, name="add_trainer"),
    path("entrenador/edit/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("entrenador/delete/<int:id>/", views.delete_trainer, name="delete_trainer"),
]