from django.urls import path
from .views import inicio,paquetes,formulario, agendarTailandia,agendarNatal, about, contacto, blog, blogD



urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path ('paq/', paquetes, name="Paquetes"),
    path('form/', formulario, name="Formulario"),
    path('tai/', agendarTailandia, name="Tailandia"),
    path('nat/', agendarNatal, name="Natal"),
    path('about/', about, name="About"),
    path('cont/', contacto, name="Contacto"),
    path('blog/', blog, name="Blog"),
    path('blogD/', blogD, name="BlogDetail")
    ]
