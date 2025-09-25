# juego/urls.py
from django.urls import path
from . import views
# YA MANDEN A LA CASA 
urlpatterns = [
    path('', views.inicio_juego, name='inicio'),
    path('pregunta/', views.pregunta_aleatoria, name='pregunta'),
    # Otras URLs como 'resultado/', 'puntuacion/', etc.
]