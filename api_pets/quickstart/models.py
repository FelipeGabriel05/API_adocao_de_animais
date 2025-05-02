from django.db import models

class  Animais(models.Model):
    Nome_do_pet = models.CharField(max_length=30, null=False, blank=False)
    tipo_de_pet = models.CharField(max_length=40, null=False, blank=False)
    raca = models.CharField(max_length=40, null=False, blank=False)
    foto_pet = models.ImageField(upload_to="images", null=False, blank=False)
    data_da_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pets'
        ordering = ['id']