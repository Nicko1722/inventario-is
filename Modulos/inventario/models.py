from django.db import models

# Create your models here.


class Provedor(models.Model):

    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria)
    provedor = models.ForeignKey(Provedor)
    unidades = models.PositiveIntegerField()