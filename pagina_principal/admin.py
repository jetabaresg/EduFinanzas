from django.contrib import admin
from .models import Modulo, Contenido, Feedback

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_creacion')
    search_fields = ('titulo',)
    ordering = ('titulo',)

@admin.register(Contenido)
class ContenidoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modulo', 'tipo', 'fecha_creacion')
    list_filter = ('modulo', 'tipo')
    search_fields = ('titulo',)
    ordering = ('modulo',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_creacion')
    ordering = ('-fecha_creacion',)
    search_fields = ('nombre', 'email')
