from django.shortcuts import render,redirect
from UserApp.forms import formulario_f, UserRegisterForm,UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import ImagenForm
from .models import Imagen

def formulario (request):
 
      if request.method == "POST":
 
            miFormulario = formulario_f (request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
               
                  paquetes = paquetes(nombre=informacion["nombre"], cantidad=informacion["cantidad"])
                  paquetes.save()
                  return render(request, "UserApp/index.html")
      else:
            miFormulario = formulario_f()
 
      return render(request, "UserApp/formulario.html", {"miFormulario": miFormulario})


def login_request (request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"UserApp/index.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"UserApp/index.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"UserApp/index.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"UserApp/login.html", {'form':form} )


def register (request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"UserApp/index.html" ,  {"mensaje":f"{username} Usuario Creado :)"})


      else:
            form = UserRegisterForm()          

      return render(request,"UserApp/register.html" ,  {"form":form})

@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  if informacion["password1"] != informacion["password2"]:
                        datos= {
                              'first_name':usuario.first_name,
                              'email':usuario.email
                        }
                        miFormulario=UserEditForm(initial=datos)
                   #Datos que se modificarán
                  else:
                        usuario.email=informacion['email']
      
                  usuario.set_pasword = (informacion['password1'])
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']

                  usuario.save()

                  return render(request, "UserApp/index.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea
      else: 
          datos= {
          'first_name':usuario.first_name,
          'email':usuario.email    
      }
      #Creo el formulario con los datos que voy a modificar
      miFormulario= UserEditForm(initial=datos) 

      #Voy al html que me permite editar
      return render(request, "UserApp/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


def upload_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)#aquí mellega toda la información del html
        if form.is_valid(): #Si pasó la validación de Django
            imagen = Imagen (imagen=request.FILES['imagen'])
            imagen.save()
            return redirect('home')
    else:
        form = ImagenForm()
    return render(request, 'upload.html', {'form': form})#Vuelvo al inicio o a donde quieran


def pag_construccion (request):
      return render (request, "TurismoApp/construccion.html")

