from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def recipes_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipes-list.html')

def recipes_add_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-add.html')

def recipes_edit_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-edit.html')

def recipes_delete_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-delete.html')

def recipes_detail_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/recipe-detail.html')
