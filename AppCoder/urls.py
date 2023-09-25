from django.urls import path
from AppCoder.views import * # ponemos un asterisco para que importe TODAS las vistas de AppCoder.views

urlpatterns = [
       path("", inicio, name="Inicio"),
       path('propiedades/', propiedad, name="Propiedades"),
       path('compradores/', comprador, name="Compradores"),
       path('agentesInmobiliarios/', agenteInmobiliario, name="AgentesInmobiliarios"),
       path('propiedadFormulario/', propiedadFormulario, name="FormularioPropiedad"),
       path('busquedaPropiedad/', busquedaPropiedad, name="BusquedaPropiedad"),
       path('resultados/', resultados, name="ResultadosBusqueda"),
]