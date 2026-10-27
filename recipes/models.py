from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=15
    )

    def __str__(self) -> str:
        return self.name

class Recipe(models.Model):
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
    instructions = models.TextField()
    time = models.IntegerField()
    ingredients = models.ManyToManyField(
        to='ingredients.Ingredient'
    )
    date_of_publication = models.DateField(
        auto_now=True
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='recipes',
        null=True,
        blank=True,
    )
