from django.urls import path
from .views import PetsView, PetActions

urlpatterns = [
    path('pets', PetsView.as_view(), name='pets'),
    path('pet/<int:pk>/', PetActions.as_view(), name='pet')
]