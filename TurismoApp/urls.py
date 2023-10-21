from django.urls import path
from .views import inicio,paquetes,tailandia, natal,formulario



urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path ('paq/', paquetes, name="Paquetes"),
    path('tai/', tailandia, name="Tailandia"),
    path('nat/', natal, name="Natal"),
    path('form/', formulario, name="Formulario")
    ]
