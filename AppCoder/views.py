from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Propiedad, Comprador, AgenteInmobiliario    # Importo las clases de models.py a views.py
from AppCoder.forms import PropiedadFormulario, CompradorFormulario, AgenteInmobiliarioFormulario

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def propiedad(request):

    prop1 = Propiedad(
        nombre="Casa Forida", 
        ubicacion = "Recoleta", 
        precio = 100000, 
        tipo_propiedad = "casa", 
        descripcion = "Excelente casa de 4 ambientes, ideal para una familia"
        ) # acá estanciamos la clase para crear un objeto

    prop1.save()

    return HttpResponse(f"La propiedad que has creado es una {prop1.tipo_propiedad} llamada {prop1.nombre}, ubicada en {prop1.ubicacion}, con un precio de ${prop1.precio} dolares.")

def comprador(request):
    return render(request, "AppCoder/compradores.html")

def agenteInmobiliario(request):
    return render(request, "AppCoder/agentesInmobiliarios.html")

def propiedadFormulario(request):   #creamos una nueva vista para crear el formulario correspondiente (para agregar nuevas propiedades)
    
    if request.method == "POST":    #despues de dar click al boton de enviar
        
        formulario1 = PropiedadFormulario(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            propiedad = Propiedad(
                nombre=info["nombre"],
                ubicacion=info["ubicacion"],
                precio=info["precio"],
                tipo_propiedad=info["tipo_propiedad"],
                descripcion=info["descripcion"],
                )
                
            propiedad.save()

            return render(request, "AppCoder/inicio.html")
    else:

        formulario1 = PropiedadFormulario()
    
    
    return render(request, "AppCoder/propiedadFormulario.html", {"form1":formulario1})


def compradorFormulario(request):   #creamos una nueva vista para crear el formulario correspondiente (para agregar nuevas propiedades)
    
    if request.method == "POST":    #despues de dar click al boton de enviar
        
        formulario1 = CompradorFormulario(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            comprador = Comprador(
                nombre=info["nombre"],
                email=info["email"],
                )
                
            comprador.save()

            return render(request, "AppCoder/inicio.html")
    else:

        formulario1 = CompradorFormulario()
    
    
    return render(request, "AppCoder/compradorFormulario.html", {"form1":formulario1})


def agenteInmobiliarioFormulario(request):   #creamos una nueva vista para crear el formulario correspondiente (para agregar nuevas propiedades)
    
    if request.method == "POST":    #despues de dar click al boton de enviar
        
        formulario1 = AgenteInmobiliarioFormulario(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            agenteInmobiliario = AgenteInmobiliario(
                nombre=info["nombre"],
                email=info["email"],
                )
                
            agenteInmobiliario.save()

            return render(request, "AppCoder/inicio.html")
    else:

        formulario1 = AgenteInmobiliarioFormulario()
    
    
    return render(request, "AppCoder/agenteInmobiliarioFormulario.html", {"form1":formulario1})











def busquedaPropiedad(request):

    return render(request, "AppCoder/inicio.html")


def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        ubicacion = Propiedad.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/inicio.html", {"nombre":nombre, "ubicacion":ubicacion})
    
    else:

        respuesta = "No has enviado datos."

    return HttpResponse(respuesta)
    
    return HttpResponse(f"Estás buscando la propiedad llamada: {request.GET['nombre']}")