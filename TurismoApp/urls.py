from django.urls import path
from .views import inicio,paquetes,formulario, agendarTailandia,agendarNatal, about, contacto, blog, blogD, ComentarioPagina



urlpatterns = [
    path('', inicio, name="Inicio"),
    path ('paq/', paquetes, name="Paquetes"),
    path('form/', formulario, name="Formulario"),
    path('tai/', agendarTailandia, name="Tailandia"),
     path('comentario/<int:pk>/', ComentarioPagina.as_view(), 
          name='crear_comentario'),
    path('nat/', agendarNatal, name="Natal"),
    path('about/', about, name="About"),
    path('cont/', contacto, name="Contacto"),
    path('blog/', blog, name="Blog"),
    path('blogD/', blogD, name="BlogDetail"),
   
    ]
