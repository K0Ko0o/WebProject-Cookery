from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def ingredients_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredients-list.html')

def ingredients_add_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-add.html')

def ingredients_edit_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-edit.html')

def ingredients_delete_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-delete.html')

def ingredients_detail_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'ingredients/ingredient-detail.html')

