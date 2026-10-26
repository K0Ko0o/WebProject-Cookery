from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from recipes.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes.models import Recipe


def recipes_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipes-list.html')

def recipes_add_view(request: HttpRequest) -> HttpResponse:
    form = RecipeCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('common:homepage')

    context = {
        'form': form
    }

    return render(request, 'recipes/recipe-add.html', context)

def recipes_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = get_object_or_404(Recipe, id=pk)
    form = RecipeEditForm(request.POST or None, request.FILES or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('recipe:detail', recipe.id)

    context = {
        'form': form
    }

    return render(request, 'recipes/recipe-edit.html', context)

def recipes_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = get_object_or_404(Recipe, id=pk)
    form = RecipeDeleteForm(request.POST or None, request.FILES or None, instance=recipe)

    if request.POST:
        recipe.delete()
        return redirect('common:homepage')

    context = {
        'form': form
    }

    return render(request, 'recipes/recipe-delete.html', context)

def recipes_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = Recipe.objects.prefetch_related('ingredients').get(id=pk)

    context = {
        "recipe": recipe
    }

    return render(request, 'recipes/recipe-detail.html', context)
