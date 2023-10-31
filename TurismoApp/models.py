from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class inicio (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    fechaDeSalida = models.DateField()

class paquetes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeSalida = models.DateField()
    cantidad = models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class Tailandia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    fechaDeSalida = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.ForeignKey(
    Tailandia, related_name='comentarios', on_delete=models.CASCADE, null=True)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def _str_(self):
        return '%s - %s' % (self.nombre, self.comentario)
    

class natal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    fechaDeSalida = models.DateField()

