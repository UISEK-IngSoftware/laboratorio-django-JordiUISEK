# Generated by Django 4.2.9 on 2025-05-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_pokemon_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
