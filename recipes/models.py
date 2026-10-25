from django.db import models

class Recipe(models.Model):
    id = models
    name = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to='recipe-images/',
        blank=True,
        null=True,
    )
    description = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )
    instructions = models.TextField(
        default='Empty'
    )
    time = models.IntegerField(
        default=0
    )
    ingredients = models.ManyToManyField(
        to='ingredients.Ingredient'
    )
    date_of_publication = models.DateField(
        auto_now=True
    )