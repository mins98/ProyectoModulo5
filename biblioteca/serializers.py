
from rest_framework import serializers
from .models import Biblioteca, MaterialBibliografico, Prestamo


class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = "__all__"
        
class MaterialBibliograficoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialBibliografico
        fields = "__all__"
        
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"
        
class ContactSerializer(serializers.Serializer):
        id = serializers.IntegerField() 
        def getId(self): 
      
            idRet=self.initial_data['id'] 
            return idRet
