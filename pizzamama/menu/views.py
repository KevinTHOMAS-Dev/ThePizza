from django.shortcuts import render
from .models import Pizza
from django.core import serializers
from django.http import HttpResponse


# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()

    return render(request,"menu/index.html", {"pizzas": pizzas})

def api_get_pizzas(request):
    pizzas = Pizza.objects.all()
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)