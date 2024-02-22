from django.shortcuts import render
from .models import Pizza



# Create your views here.

def index(request):
    pizzas= Pizza.objects.all()

    return render(request,"menu/index.html", {"pizzas": pizzas})

