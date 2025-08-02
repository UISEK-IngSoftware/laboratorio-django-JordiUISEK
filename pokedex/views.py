from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib import messages
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    template_name = 'login_form.html'

def custom_logout(request):
    logout(request)
    return redirect('pokedex:index')
    
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

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
            
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, f'Pokemon "{pokemon.name}" actualizado correctamente.')
            return redirect('pokedex:pokemon', id=id)
    else:
        form = PokemonForm(instance=pokemon)
    return render (request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(pk=id)
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
            
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, id: int):
    trainer = Trainer.objects.get(pk=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Entrenador "{trainer.name}" actualizado correctamente.')
            return redirect('pokedex:trainer', id=id)
    else:
        form = TrainerForm(instance=trainer)
    return render (request, 'trainer_form.html', {'form': form})
        
@login_required
def delete_trainer(request, id: int):
    trainer = Trainer.objects.get(pk=id)
    trainer.delete()
    return redirect('pokedex:index')
