from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from ingredients.forms import IngredientSearchForm
from ingredients.models import Ingredient


def ingredients_list_view(request: HttpRequest) -> HttpResponse:
    all_ingredients = Ingredient.objects.all()
    form = IngredientSearchForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data['query']
        category = form.cleaned_data['category']

        if query:
            all_ingredients = all_ingredients.filter(name__icontains=query)

        if category:
            all_ingredients = all_ingredients.filter(category=category)

    context = {
        'all_ingredients': all_ingredients,
        'form': form,
    }

    return render(request, 'ingredients/ingredients-list.html', context)

def ingredients_add_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-add.html')

def ingredients_edit_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-edit.html')

def ingredients_delete_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-delete.html')

def ingredients_detail_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-detail.html')

