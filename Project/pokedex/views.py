from django.shortcuts import render
from .models import Pokemon

# Create your views here.

def mostrar_pokemon(request):
    nome = Pokemon.objects.all()
    
    context = {
        'nome': nome
    }

    return render(request, '', context)