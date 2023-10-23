from django import forms


class formulario_f (forms.Form):
    paquetes = forms.CharField()
    cantidadPersonas = forms.IntegerField()

class formulario_t (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)
    fechaDeSalida = forms.DateField()

class formulario_N (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)
    fechaDeSalida = forms.DateField()    

class formulario_c (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)