from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.order_by("name")
    trainers = Trainer.objects.order_by("name")
    template = loader.get_template('index.html')
    params = {
        'title': 'Pokedex', 
        'subtitle': 'Mi Pokedex', 
        'list_pokemons': 'Lista de Pokemons', 
        'pokemons': pokemons, 
        'list_trainers': 'Lista de entreandores', 
        'trainers': trainers
    }
    return HttpResponse(template.render(params, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, id: int):
    trainer = Trainer.objects.get(pk=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))