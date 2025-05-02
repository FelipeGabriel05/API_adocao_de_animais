from rest_framework import serializers
from .models import Animais

class Animais_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Animais
        fields = (
            'id',
            'Nome_do_pet',
            'tipo_de_pet',
            'raca',
            'foto_pet',
            'data_da_criacao'
        )

