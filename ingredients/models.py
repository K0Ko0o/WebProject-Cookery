from django.db import models

class Supermarket(models.Model):
    name = models.CharField(
        max_length=15
    )

class Ingredient(models.Model):
    name = models.CharField(
        max_length=50,
    )
    image = models.ImageField(
        upload_to='ingredient-images',
        null=True,
        blank=True,
    )
    calories_per_100_grams = models.IntegerField()

    supermarket = models.ForeignKey(
        to=Supermarket,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name