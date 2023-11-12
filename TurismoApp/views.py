from django.shortcuts import render, redirect
from TurismoApp.forms import formulario_f, formulario_t,formulario_N, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Tailandia, Comentario, natal, paquetes



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
    paquetes_tailandia = Tailandia.objects.all()
    paquete_comments = Comentario.objects.all()
    return render (request, "TurismoApp/paquetes.html",{"paquetes_tailandia": paquetes_tailandia, "paquete_comments": paquete_comments, "form": ComentarioForm()})
    


def agendarTailandia(request):
      if request.method == 'POST':

            miTai = formulario_t (request.POST) 
    
            if miTai.is_valid():
               informacion = miTai.cleaned_data
               tailandia =  Tailandia(
                 nombre=informacion['nombre'], apellido=informacion['apellido'], fechaDeSalida=informacion['fechaDeSalida'], email=informacion['fechaDeSalida'], user=request.user)
               tailandia.save()
            return redirect('Paquetes')
      else:
        miTai = formulario_N()

      return render(request, "TurismoApp/tailandia.html", {"miTai": miTai})  
  
             
class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name= 'tu_template.html'
    success_url = reverse_lazy('Paquetes')

    def form_valid(self, form):
        form.instance.user =  self.request.user
        tailandia_id = self.kwargs['pk']
        form.instance.comentario= Tailandia.objects.get(pk=tailandia_id)
        return super(ComentarioPagina, self).form_valid(form)


       

def agendarNatal (request):
 
      if request.method == "POST":
 
            miNat = formulario_N (request.POST) 
            print(miNat)
 
            if miNat.is_valid():
                  informacion = miNat.cleaned_data
                  
                  evento_natal = natal(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"], fechaDeSalida=informacion["fechaDeSalida"])
                  evento_natal.save()
                  return redirect ('Natal')
                  
      else:
            miNat = formulario_N()
 
      return render(request, "TurismoApp/natal.html", {"miNat": miNat, "paquetes_natal":natal.objects.all()})


     

def formulario (request):
 
      if request.method == "POST":
 
            miFormulario = formulario_f (request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
               
                  paquete = paquetes(
                       nombre=informacion["nombre"], cantidad=informacion["cantidad"])
                  paquete.save()
                  return render(request, "TurismoApp/index.html")
      else:
            miFormulario = formulario_f()
 
      return render(request, "TurismoApp/formulario.html", {"miFormulario": miFormulario})





