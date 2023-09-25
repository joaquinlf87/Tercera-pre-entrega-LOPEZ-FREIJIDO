from django import forms


class PropiedadFormulario(forms.Form):

    nombre = forms.CharField()
    ubicacion = forms.CharField()
    precio = forms.IntegerField()
     # Definir opciones para el campo tipo_propiedad
    OPCIONES_TIPO_PROPIEDAD = (
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('terreno', 'Terreno'),
        ('local', 'Local Comercial'),
        ('otro', 'Otro')
    )
    tipo_propiedad = forms.ChoiceField(choices=OPCIONES_TIPO_PROPIEDAD)
    descripcion = forms.CharField()


class CompradorFormulario(forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField(required=False)

class AgenteInmobiliarioFormulario(forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField(required=False)