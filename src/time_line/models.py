from django.db import models

from django.db import models

class Freelancer(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name='calificaciones')
    estrellas = models.IntegerField()  # Número de estrellas, de 1 a 5
    descripcion = models.TextField(blank=True, null=True)  # Comentario opcional del cliente
    fecha_calificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.freelancer.nombre} - {self.estrellas} Estrellas'

