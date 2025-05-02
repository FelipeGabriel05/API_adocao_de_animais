from .serializers import Animais_Serializer
from .models import Animais
from rest_framework import generics

class PetsView(generics.ListCreateAPIView):
    queryset = Animais.objects.all()
    serializer_class = Animais_Serializer

class PetActions(generics.RetrieveDestroyAPIView):
    queryset = Animais.objects.all()
    serializer_class = Animais_Serializer
