from django import forms
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'weight', 'height', 'description', 'picture']
        widgets = {
            'name': forms.TextInput(attrs=({'class': 'form-control', 'placeholder': 'Nombre del pokemon'})),
            'type': forms.TextInput(attrs=({'class': 'form-control', 'placeholder': 'Tipo de elemento'})),
            'weight': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': 0})),
            'height': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': 0})),
            'description': forms.Textarea(attrs=({'class': 'form-control'})),
            'picture': forms.FileInput(attrs=({
                'class': 'form-control',
                'id': 'image_field'
            }))
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'age', 'weight', 'height', 'catch', 'description', 'picture']
        widgets = {
            'name': forms.TextInput(attrs=({'class': 'form-control', 'placeholder': 'Nombre del entrenador'})),
            'age': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': 0})),
            'weight': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': 0})),
            'height': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': 0})),
            'catch': forms.NumberInput(attrs=({'class': 'form-control', 'min': 0, 'placeholder': 0})),
            'description': forms.Textarea(attrs=({'class': 'form-control'})),
            'picture': forms.FileInput(attrs=({
                'class': 'form-control',
                'id': 'image_field'
            }))
        }