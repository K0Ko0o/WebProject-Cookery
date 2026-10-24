from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

def homepage_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/homepage.html' )
