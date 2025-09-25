from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juego.urls')), 
    # empieza con s y termina en y jajajajaj ok no 
]