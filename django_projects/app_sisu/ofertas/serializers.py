from dataclasses import field
from ofertas.models import Universidade
from rest_framework import serializers


class UniversidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Universidade
        # fields = ('id', 'sigla', 'nome')
        fields = '__all__'