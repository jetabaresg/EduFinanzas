from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Modulo, Contenido, Feedback, Progreso,Pregunta, OpcionRespuesta, IntentoEvaluacion, RespuestaUsuario


# ===========================
#   PÁGINAS PRINCIPALES
# ===========================
def home(request):
    return render(request, "home.html")


def acerca(request):
    return render(request, "acerca.html")


# ===========================
#         APRENDE
# ===========================
def aprende(request):
    """
    Muestra todos los módulos publicados con su progreso.
    """
    modulos = Modulo.objects.filter(publicado=True).order_by("orden")
    
    # Si el usuario está autenticado, agregar información de progreso
    if request.user.is_authenticated:
        for modulo in modulos:
            # Un módulo se considera completado SOLO si pasó la evaluación (≥ 70%)
            progreso = Progreso.objects.filter(
                usuario=request.user,
                modulo=modulo,
                completado=True
            ).first()
            
            # Agregar datos al módulo
            modulo.progreso_usuario = progreso
            modulo.completado = progreso and progreso.completado
    else:
        # Usuario no autenticado
        for modulo in modulos:
            modulo.progreso_usuario = None
            modulo.completado = False

    contexto = {
        "mensaje": "Selecciona un módulo y empieza a aprender:",
        "modulos": modulos,
    }
    return render(request, "aprende.html", contexto)


def detalle_modulo(request, modulo_id):
    """
    Muestra los contenidos de un módulo y consulta el progreso del usuario.
    """
    modulo = get_object_or_404(Modulo, id=modulo_id)
    contenidos = modulo.contenidos.all().order_by("orden")

    progreso_modulo = None

    # Si el usuario está autenticado, obtenemos o creamos el progreso del módulo
    if request.user.is_authenticated:
        progreso_modulo, _ = Progreso.objects.get_or_create(
            usuario=request.user,
            modulo=modulo
        )

    contexto = {
        "modulo": modulo,
        "contenidos": contenidos,
        "progreso_modulo": progreso_modulo,
    }
    return render(request, "detalle_modulo.html", contexto)


def ver_contenido(request, contenido_id):
    """
    Muestra un contenido individual, convierte enlaces de YouTube a embed
    y actualiza el progreso del usuario automáticamente.
    """
    contenido = get_object_or_404(Contenido, id=contenido_id)
    modulo = contenido.modulo

    # ==============================
    #   CONVERTIR URL DE YOUTUBE
    # ==============================
    embed_url = None

    if contenido.url_video:
        url = contenido.url_video.strip()

        # Caso típico: https://www.youtube.com/watch?v=xxxxx
        if "youtube.com/watch" in url:
            try:
                video_id = url.split("v=")[-1].split("&")[0]
                embed_url = f"https://www.youtube.com/embed/{video_id}"
            except:
                embed_url = None

        # Caso corto: https://youtu.be/xxxxx
        elif "youtu.be" in url:
            try:
                video_id = url.split("/")[-1].split("?")[0]
                embed_url = f"https://www.youtube.com/embed/{video_id}"
            except:
                embed_url = None

    # ==============================
    #     PREGUNTAS DEL QUIZ
    # ==============================
    preguntas = None
    if contenido.tipo == 'quiz':
        preguntas = contenido.preguntas.all().order_by('orden')

    # ==============================
    #     PROGRESO AUTOMÁTICO
    # ==============================
    if request.user.is_authenticated:
        # Actualizar progreso del módulo (marcar con fecha de acceso)
        progreso, _ = Progreso.objects.get_or_create(
            usuario=request.user,
            modulo=modulo
        )
        progreso.fecha_completado = timezone.now()
        progreso.save()

    contexto = {
        "contenido": contenido,
        "modulo": modulo,
        "embed_url": embed_url,
        "preguntas": preguntas,
    }

    return render(request, "contenido_detalle.html", contexto)
# ===========================
#         FEEDBACK
# ===========================
def feedback(request):
    """
    Procesa sugerencias, reclamos, mensajes y calificaciones.
    """
    if request.method == "POST":
        tipo = request.POST.get("tipo")
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")
        calificacion = request.POST.get("calificacion")

        # Validación básica
        if not all([tipo, nombre, email, asunto, mensaje]):
            messages.error(request, "Por favor completa todos los campos obligatorios.")
            return render(request, "feedback.html")

        Feedback.objects.create(
            tipo=tipo,
            nombre=nombre,
            email=email,
            asunto=asunto,
            mensaje=mensaje,
            calificacion=calificacion if calificacion else None,
        )

    return render(request, "feedback.html")


def procesar_evaluacion(request, contenido_id):
    """
    Procesa las respuestas y calcula el puntaje
    """
    # Verificar que el usuario está autenticado
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para hacer evaluaciones.")
        return redirect('login')
    
    if request.method == 'POST':
        contenido = get_object_or_404(Contenido, id=contenido_id, tipo='quiz')
        
        # Crear o recuperar intento (crear si no existe)
        intento, created = IntentoEvaluacion.objects.get_or_create(
            usuario=request.user,
            contenido=contenido,
            completado=False,
            defaults={'puntaje_maximo': contenido.preguntas.count()}
        )
        
        puntaje_total = 0
        respuestas_correctas = 0
        total_preguntas = contenido.preguntas.count()
        
        # Procesar cada pregunta
        for pregunta in contenido.preguntas.all():
            opcion_id = request.POST.get(f'pregunta_{pregunta.id}')
            
            if opcion_id:
                try:
                    opcion_seleccionada = OpcionRespuesta.objects.get(id=opcion_id)
                    es_correcta = opcion_seleccionada.es_correcta
                    
                    # Guardar respuesta del usuario
                    RespuestaUsuario.objects.create(
                        intento=intento,
                        pregunta=pregunta,
                        opcion_seleccionada=opcion_seleccionada,
                        es_correcta=es_correcta
                    )
                    
                    if es_correcta:
                        puntaje_total += pregunta.puntos
                        respuestas_correctas += 1
                        
                except OpcionRespuesta.DoesNotExist:
                    # Opción no válida
                    pass
        
        # Actualizar intento
        intento.puntaje_obtenido = puntaje_total
        intento.completado = True
        intento.fecha_fin = timezone.now()
        intento.save()
        
        # Marcar módulo como completado si se aprobó
        modulo = contenido.modulo
        progreso, _ = Progreso.objects.get_or_create(
            usuario=request.user,
            modulo=modulo
        )
        
        # Aprobar si obtiene 70% o más
        porcentaje = (puntaje_total / (total_preguntas * 1)) * 100 if total_preguntas > 0 else 0
        if porcentaje >= 70:
            progreso.completado = True
            progreso.fecha_completado = timezone.now()
            progreso.save()
        
        contexto = {
            'contenido': contenido,
            'modulo': modulo,
            'puntaje_obtenido': puntaje_total,
            'puntaje_maximo': total_preguntas,
            'respuestas_correctas': respuestas_correctas,
            'total_preguntas': total_preguntas,
            'porcentaje': porcentaje,
            'aprobado': porcentaje >= 70,
        }
        
        return render(request, 'evaluacion/resultados.html', contexto)
    
    return redirect('detalle_modulo', modulo_id=contenido.modulo.id)


def ver_progreso(request):

    # Para usuarios autenticados, mostrar sus datos reales
    if request.user.is_authenticated:
        modulos_progreso = Progreso.objects.filter(usuario=request.user).select_related('modulo')
        total_modulos = Modulo.objects.filter(publicado=True).count()
        modulos_completados = modulos_progreso.filter(completado=True).count()
        intentos = IntentoEvaluacion.objects.filter(usuario=request.user, completado=True)
        modulos_pendientes = total_modulos - modulos_completados
    else:
        # Para usuarios no autenticados, mostrar datos de ejemplo o vacíos
        modulos = Modulo.objects.filter(publicado=True)
        total_modulos = modulos.count()
        modulos_completados = 0
        modulos_pendientes = total_modulos
        modulos_progreso = []
        intentos = []
    
    contexto = {
        'modulos_progreso': modulos_progreso,
        'total_modulos': total_modulos,
        'modulos_completados': modulos_completados,
        'modulos_pendientes': modulos_pendientes,
        'intentos': intentos,
        'porcentaje_completado': (modulos_completados / total_modulos * 100) if total_modulos > 0 else 0,
    }
    
    return render(request, 'evaluacion/progreso.html', contexto)

def abandonar_evaluacion(request, intento_id):
    """
    Flujo alternativo: Usuario abandona la evaluación
    """
    intento = get_object_or_404(IntentoEvaluacion, id=intento_id, usuario=request.user)
    
    # Marcar como completado pero con puntaje 0
    intento.completado = True
    intento.fecha_fin = timezone.now()
    intento.puntaje_obtenido = 0
    intento.save()
    
    messages.info(request, "Has abandonado la evaluación. Puedes intentarlo nuevamente cuando quieras.")
    return redirect('detalle_modulo', modulo_id=intento.contenido.modulo.id)