from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from recipes.forms import RecipeCreateForm


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

def recipes_edit_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-edit.html')

def recipes_delete_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-delete.html')

def recipes_detail_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-detail.html')
