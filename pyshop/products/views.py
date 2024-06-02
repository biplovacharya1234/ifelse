from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("This is product page")


def trending(request):
    return HttpResponse("This is trending products")
