from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe


def homepage_view(request: HttpRequest) -> HttpResponse:
    all_recipes = Recipe.objects.all()

    context = {
        'all_recipes': all_recipes
    }

    return render(request, 'common/homepage.html', context)
