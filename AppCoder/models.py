from django.db import models

# Create your models here.
class Propiedad(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.nombre} ------ Ubicacion: {self.ubicacion} ------ Precio: {self.precio}"
    
    TIPOS_DE_PROPIEDAD = (
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('terreno', 'Terreno'),
        ('local_comercial', 'Local Comercial'),
        ('otro', 'Otro'),
    )

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_propiedad = models.CharField(max_length=20, choices=TIPOS_DE_PROPIEDAD)
    descripcion = models.TextField()

class Comprador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class AgenteInmobiliario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()