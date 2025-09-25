from django.shortcuts import render, get_object_or_404
from .models import Pregunta
import random

def inicio_juego(request):
    # Lógica para mostrar la pantalla de inicio
    return render(request, 'juego/inicio.html')

def pregunta_aleatoria(request):
    preguntas = list(Pregunta.objects.all())
    pregunta_actual = random.choice(preguntas)
    # Lógica para manejar el envío de la respuesta
    # ...
    return render(request, 'juego/pregunta.html', {'pregunta': pregunta_actual})