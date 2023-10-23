from django.shortcuts import render
from TurismoApp.forms import formulario_f, formulario_t,formulario_N



# Create your views here.
def inicio(request):
    return render (request, "TurismoApp/index.html")

def about(request):
    return render (request, "TurismoApp/about.html")

def contacto(request):
    return render (request, "TurismoApp/contacto.html")

def blog (request):
    return render (request, "TurismoApp/blog.html")

def blogD (request):
    return render (request, "TurismoApp/blogDetalle.html")


def paquetes(request):
    return render (request,"TurismoApp/paquetes.html")


def agendarTailandia(request):
      if request.method == 'POST':

            miTai = formulario_t (request.POST) 
            print(miTai)

            if miTai.is_valid():
                  informacion = miTai.cleaned_data

            tailandia =  tailandia(request.post['nombre']),(request.post['apellido']),(request.post['nombre'],(request.post['apellido']))
            tailandia.save()
 
            return render(request, "TurismoApp/tailandia.html")
      else:
            miTai = formulario_N()
 
      return render(request, "TurismoApp/tailandia.html", {"miTai": miTai})
 

def agendarNatal (request):
 
      if request.method == "POST":
 
            miNat = formulario_N (request.POST) 
            print(miNat)
 
            if miNat.is_valid():
                  informacion = miNat.cleaned_data
               
                  natal = natal(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"], fechaDeSalida=informacion["fechaDeSalida"])
                  natal.save()
                  return render(request, "TurismoApp/natal.html")
      else:
            miNat = formulario_N()
 
      return render(request, "TurismoApp/natal.html", {"miNat": miNat})


     

def formulario (request):
 
      if request.method == "POST":
 
            miFormulario = formulario_f (request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
               
                  paquetes = paquetes(nombre=informacion["nombre"], cantidad=informacion["cantidad"])
                  paquetes.save()
                  return render(request, "TurismoApp/index.html")
      else:
            miFormulario = formulario_f()
 
      return render(request, "TurismoApp/formulario.html", {"miFormulario": miFormulario})






