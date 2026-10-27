from difflib import context_diff

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from ingredients.forms import IngredientSearchForm, IngredientCreateForm, IngredientEditForm, IngredientDeleteForm
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
    form = IngredientCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('common:homepage')

    context = {
        'form': form
    }

    return render(request, 'ingredients/ingredient-add.html', context)

def ingredients_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, id=pk)
    form = IngredientEditForm(request.POST or None, request.FILES or None, instance=ingredient)

    if form.is_valid():
        form.save()
        return redirect('common:homepage')

    context = {
        'form': form
    }

    return render(request, 'ingredients/ingredient-edit.html', context)

def ingredients_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, id=pk)
    form = IngredientDeleteForm(request.POST or None, request.FILES or None, instance=ingredient)

    if request.POST:
        ingredient.delete()
        return redirect('common:homepage')

    context = {
        'form': form
    }

    return render(request, 'ingredients/ingredient-delete.html', context)

def ingredients_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, id=pk)

    context = {
        "ingredient": ingredient
    }

    return render(request, 'ingredients/ingredient-detail.html', context)

