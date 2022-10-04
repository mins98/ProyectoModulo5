from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import BibliotecaSerializer, MaterialBibliograficoSerializer, PrestamoSerializer,ContactSerializer
from .models import Biblioteca,MaterialBibliografico,Prestamo
from datetime import datetime  
from django.core import serializers

class BibliotecaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    
class MaterialBibliograficoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = MaterialBibliografico.objects.all()
    serializer_class = MaterialBibliograficoSerializer
    
class MaterialBibliograficoGetAndDeleteView(generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = MaterialBibliografico.objects.all()
    serializer_class = MaterialBibliograficoSerializer
    
class PrestamoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    

@api_view(["POST"])
def devolver_prestamo(request):
    cs= ContactSerializer(data=request.data)
    if cs.is_valid():
        idChange=cs.getId()
        Prestamo.objects.filter(pk=idChange).update(fechaDevolucion=datetime.now())
        prestamoCambiado= Prestamo.objects.filter(pk=idChange)
        qs_json = serializers.serialize('json', prestamoCambiado)
        return JsonResponse({
            "mensaje":"Prestamo devuelto correctamente",
            "prestamo":qs_json
            }, status=200) 
    else:
        return JsonResponse({"mensaje": cs.errors}, status=200) 

    