from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    opcion_a = models.CharField(max_length=100)
    opcion_b = models.CharField(max_length=100)
    opcion_c = models.CharField(max_length=100)
    opcion_d = models.CharField(max_length=100)
    respuesta_correcta = models.CharField(max_length=100)

    def __str__(self):
        return self.pregunta_texto