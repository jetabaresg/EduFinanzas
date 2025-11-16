from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Modulo, Contenido, Feedback, Progreso


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
    Muestra todos los módulos publicados.
    """
    modulos = Modulo.objects.filter(publicado=True).order_by("orden")

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
    y actualiza el progreso del usuario.
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
    #     PROGRESO DEL USUARIO
    # ==============================
    if request.user.is_authenticated:
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
