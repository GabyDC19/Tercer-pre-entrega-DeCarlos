from django.urls import path
from .views import inicio,paquetes,formulario, agendarTailandia,agendarNatal



urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path ('paq/', paquetes, name="Paquetes"),
    path('form/', formulario, name="Formulario"),
    path('tai/', agendarTailandia, name="Tailandia"),
    path('nat/', agendarNatal, name="Natal")
    ]
