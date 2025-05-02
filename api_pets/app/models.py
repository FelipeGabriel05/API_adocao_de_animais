from django.db import models

class  Animais(models.Model):
    petName = models.CharField(max_length=30, null=False, blank=False)
    petType = models.CharField(max_length=40, null=False, blank=False)
    petBreed = models.CharField(max_length=40, null=False, blank=False)
    petPhotoUrl = models.ImageField(upload_to="images", null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pets'
        ordering = ['id']