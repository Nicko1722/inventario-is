from django.db import models
from Modulos.inventario.models import Producto
from django.contrib.auth.models import User
# Create your models here.

class Entrada(models.Model):

     usuario = models.ForeignKey(User)
     producto = models.ForeignKey(Producto)
     fecha = models.DateField(auto_now_add=True)
     unidades = models.PositiveIntegerField()



