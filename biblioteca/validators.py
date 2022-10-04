from django.core.exceptions import ValidationError
from datetime import datetime  
from django.utils import timezone

def formato_CarnetBolivia(value):
    if  (not value.isdigit()) and (value[:2] !="E-" or (not value[2:].isdigit())):
        raise ValidationError(
            '%(value)s no tiene un formato válido para carnets nacionales. Formatos validos: 1111111 o E-1111111',
            params={'value': value}
        )

def fecha_menorActual(value):
    if value > datetime.date(datetime.now()):
        raise ValidationError(
        '%(value)s la fecha debe ser menor a la actual',
        params={'value': value})

def fecha_menorIgualActual(value):
    if value >= timezone.now():
        raise ValidationError(
        '%(value)s la fecha debe ser menor o igual a la actual',
        params={'value': value})

def no_cero(value):
    if value ==0:
        raise ValidationError(
        '%(value)s el valor debe ser mayor a cero',
        params={'value': value})
        
def solo_numeros(value):
    if not value.isdigit():
        raise ValidationError(
        '%(value)s no se aceptan letras ni caracteres especiales en este campo',
        params={'value': value})
       
