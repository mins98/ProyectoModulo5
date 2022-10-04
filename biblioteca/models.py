from django.db import models
from django.core.validators import MinLengthValidator
from .validators import formato_CarnetBolivia,fecha_menorActual,no_cero,solo_numeros,fecha_menorIgualActual
from datetime import datetime  

class CategoriaMaterial(models.Model):
    nombre = models.CharField(max_length=40, validators=[MinLengthValidator(5)], unique=True)
    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=30,validators=[MinLengthValidator(5)], unique=True)
    def __str__(self):
        return self.nombre
    
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=70 ,validators=[MinLengthValidator(10)], unique=True)
    horariosAtencion = models.CharField(max_length=100,validators=[MinLengthValidator(10)])
    correo = models.EmailField(max_length=45,validators=[MinLengthValidator(5)])
    numeroTelefonico = models.CharField(max_length=20,validators=[MinLengthValidator(7),solo_numeros] )
    direccion = models.CharField(max_length=200 ,validators=[MinLengthValidator(10)])
    departamento =  models.ForeignKey(Departamento, on_delete=models.CASCADE) 
    def __str__(self):
        return self.nombre
    
class MaterialBibliografico(models.Model):
    nombre = models.CharField(max_length=250,validators=[MinLengthValidator(5)]) 
    autor =models.CharField(max_length=250,validators=[MinLengthValidator(5)]) 
    pais = models.CharField(max_length=50,validators=[MinLengthValidator(4)]) 
    cantidadEjemplares = models.PositiveSmallIntegerField(validators=[no_cero]) 
    cantidadActual = models.PositiveSmallIntegerField(validators=[no_cero]) 
    fechaPublicacion = models.DateField(auto_now=False, auto_now_add=False,validators=[fecha_menorActual])
    edicion = models.CharField(max_length=45,blank=True ,validators=[MinLengthValidator(2)]) 
    idioma = models.CharField(max_length=100,validators=[MinLengthValidator(4)]) 
    categoria = models.ForeignKey(CategoriaMaterial, on_delete=models.CASCADE) 
    perteneceA = models.ForeignKey(Biblioteca, on_delete=models.CASCADE,default=1) 
    def __str__(self):
        return self.nombre
    
class Prestamo(models.Model):
    nombres = models.CharField(max_length=50 ,validators=[MinLengthValidator(3)])
    apellidos = models.CharField(max_length=50,validators=[MinLengthValidator(3)])
    correo = models.EmailField(max_length=45,validators=[MinLengthValidator(5)])
    numeroTelefonico = models.CharField(max_length=20,validators=[MinLengthValidator(7),solo_numeros])
    direccion = models.CharField(max_length=200 ,validators=[MinLengthValidator(10)])
    ci = models.CharField(max_length=10,unique=True,validators=[formato_CarnetBolivia])
    fechaPrestamo = models.DateTimeField(default=datetime.now(), validators=[fecha_menorIgualActual])
    fechaDevolucion = models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True, validators=[fecha_menorIgualActual])
    materialPrestado = models.ForeignKey(MaterialBibliografico, on_delete=models.CASCADE) 
    def __str__(self):
        return self.nombres