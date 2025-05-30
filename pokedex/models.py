from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=40, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    description = models.CharField(max_length=150, null=True)
    picture = models.ImageField(upload_to="pokemon_images", null=True)
    
    def __str__(self) -> str:
        return self.name
    
class Trainer(models.Model):
    name = models.CharField(max_length=40, null=False)
    age = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    catch = models.IntegerField(null=False)
    description = models.CharField(max_length=150, null=True)
    picture = models.ImageField(upload_to="trainer_images", null=True)
    
    def __str__(self) -> str:
        return self.name