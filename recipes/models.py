from django.db import models

class Recipe(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
    ingredients = models.ManyToManyField(
        to='recipes.Recipe'
    )
    date_of_publication = models.DateField(
        auto_now=True
    )