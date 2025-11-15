from django.db import models

class Feedback(models.Model):
    TIPO_CHOICES = [
        ('queja', 'Queja'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
        ('calificacion', 'Calificación'),
    ]
    
    CALIFICACION_CHOICES = [
        (1, '1 ⭐ - Muy Malo'),
        (2, '2 ⭐⭐ - Malo'),
        (3, '3 ⭐⭐⭐ - Regular'),
        (4, '4 ⭐⭐⭐⭐ - Bueno'),
        (5, '5 ⭐⭐⭐⭐⭐ - Excelente'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    calificacion = models.IntegerField(choices=CALIFICACION_CHOICES, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.tipo} - {self.nombre} - {self.fecha_creacion.strftime('%Y-%m-%d')}"
