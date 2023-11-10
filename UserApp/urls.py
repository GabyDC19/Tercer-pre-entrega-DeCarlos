from django.urls import path
from .views import formulario, login_request, register, editarPerfil, upload_imagen
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('form/', formulario, name="Formulario"),
    path('login/',login_request, name="Login"),
    path('reg/',register, name="Register"),
    path('logo/', LogoutView.as_view(template_name='UserApp/logout.html'), name='Logout'),
    path('edit/', editarPerfil, name="Editar"),
    path('upload/', upload_imagen, name='upload'),
]

