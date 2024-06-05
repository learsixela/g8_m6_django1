from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    image_url = models.URLField()
    edad = models.IntegerField()
    castrado = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Objeto Mascota: {self.id} - {self.nombre}" 