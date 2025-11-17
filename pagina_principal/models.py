from django.db import models
from django.core.exceptions import ValidationError


class Modulo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Módulo")
    descripcion = models.TextField(verbose_name="Descripción del módulo")
    orden = models.PositiveIntegerField(default=1, verbose_name="Orden en el curso")
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"

    def __str__(self):
        return f"{self.orden}. {self.titulo}"


class Contenido(models.Model):
    TIPO_CHOICES = [
        ('texto', 'Texto / Explicación'),
        ('video', 'Video'),
        ('pdf', 'Documento PDF'),
        ('quiz', 'Cuestionario / Evaluación'),
        ('imagen', 'Imagen'),
    ]

    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name="contenidos")
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)

    # Campo para PDFs
    archivo = models.FileField(upload_to="contenidos/", blank=True, null=True)

    # Campo para imágenes
    imagen = models.ImageField(upload_to="imagenes/", blank=True, null=True)

    # Campo para videos externos
    url_video = models.URLField(blank=True, null=True)

    orden = models.PositiveIntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.tipo == "video" and not self.url_video:
            raise ValidationError("Debes ingresar una URL si el contenido es de tipo video.")
        if self.tipo == "pdf" and not self.archivo:
            raise ValidationError("Debes adjuntar un archivo PDF.")
        if self.tipo == "imagen" and not self.imagen:
            raise ValidationError("Debes subir una imagen para este contenido.")
    def __str__(self):
        return f"{self.modulo.titulo} - {self.titulo}"


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

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def clean(self):
        if self.tipo == "calificacion" and not self.calificacion:
            raise ValidationError("Debe ingresar una calificación si el tipo es 'calificación'.")

    def __str__(self):
        return f"{self.tipo} - {self.nombre} - {self.fecha_creacion.strftime('%Y-%m-%d')}"


class Progreso(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('usuario', 'modulo')
        verbose_name = "Progreso"
        verbose_name_plural = "Progresos"

    def __str__(self):
        estado = "Completado" if self.completado else "Pendiente"
        return f"{self.usuario.username} - {self.modulo.titulo}: {estado}"

class Pregunta(models.Model):
    TIPO_CHOICES = [
        ('opcion_multiple', 'Opción Múltiple'),
        ('verdadero_falso', 'Verdadero/Falso'),
    ]
    
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE, related_name="preguntas")
    texto = models.TextField(verbose_name="Texto de la pregunta")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='opcion_multiple')
    orden = models.PositiveIntegerField(default=1)
    puntos = models.PositiveIntegerField(default=1, verbose_name="Puntos por respuesta correcta")
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
    
    def __str__(self):
        return f"{self.contenido.titulo} - Pregunta {self.orden}"


class OpcionRespuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="opciones")
    texto = models.CharField(max_length=500, verbose_name="Texto de la opción")
    es_correcta = models.BooleanField(default=False, verbose_name="¿Es correcta?")
    orden = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Opción de Respuesta"
        verbose_name_plural = "Opciones de Respuesta"
    
    def __str__(self):
        return f"{self.pregunta.texto[:50]}... - Opción {self.orden}"


class IntentoEvaluacion(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    completado = models.BooleanField(default=False)
    puntaje_obtenido = models.FloatField(default=0)
    puntaje_maximo = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Intento de Evaluación"
        verbose_name_plural = "Intentos de Evaluación"
    
    def __str__(self):
        estado = "Completado" if self.completado else "En progreso"
        return f"{self.usuario.username} - {self.contenido.titulo} - {estado}"


class RespuestaUsuario(models.Model):
    intento = models.ForeignKey(IntentoEvaluacion, on_delete=models.CASCADE, related_name="respuestas")
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_seleccionada = models.ForeignKey(OpcionRespuesta, on_delete=models.CASCADE, null=True, blank=True)
    es_correcta = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Respuesta del Usuario"
        verbose_name_plural = "Respuestas de Usuarios"
    
    def __str__(self):
        return f"{self.intento.usuario.username} - {self.pregunta.texto[:30]}..."