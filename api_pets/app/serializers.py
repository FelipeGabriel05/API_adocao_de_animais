from rest_framework import serializers
from .models import Animais

class Animais_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Animais
        fields = (
            'id',
            'petName',
            'petType',
            'petBreed',
            'petPhotoUrl',
            'createdAt'
        )