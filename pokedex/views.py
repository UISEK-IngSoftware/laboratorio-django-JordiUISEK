from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm

def index(request):
    pokemons = Pokemon.objects.order_by("name")
    trainers = Trainer.objects.order_by("name")
    template = loader.get_template('index.html')
    params = {
        'title': 'Pokedex', 
        'subtitle': 'Pokedex de Jordi',
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

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
            
    return render(request, 'pokemon_form.html', {'form': form})

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
            
    return render(request, 'trainer_form.html', {'form': form})