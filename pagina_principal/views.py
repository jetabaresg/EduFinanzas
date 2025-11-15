from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feedback 
from django.contrib import messages

BANCOS_TRADICIONALES = [
    {'id': 'BanColombia', 'nombre': 'BanColombia'},
    {'id': 'BancoBogota', 'nombre': 'Davivienda'},
]
BANCOS_DIGITALES= [
    {'id': 'Nequi', 'nombre': 'Nequi'},
    {'id': 'MiBancolombia', 'nombre': 'MiBancolombia'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def acerca(request):
    return render(request, 'acerca.html')

def aprende(request):
    
    contexto = {
        'bancos_tradicionales': BANCOS_TRADICIONALES,
        'bancos_digitales': BANCOS_DIGITALES,
        'mensaje': 'Para comenzar tu aprendizaje selecciona el banco:'
    }
    return render(request, 'aprende.html', contexto)

def banco_detalle(request, banco_id):
    banco_seleccionado = None
    for banco in BANCOS_TRADICIONALES:
        if banco['id'] == banco_id:
            banco_seleccionado = banco
            break
    
    for banco in BANCOS_DIGITALES:
        if banco['id'] == banco_id:
            banco_seleccionado = banco
            break
    
    if not banco_seleccionado:
      return render(request, 'aprende.html', {
          'bancos_tradicionales': BANCOS_TRADICIONALES,
          'bancos_digitales': BANCOS_DIGITALES,
          'error': 'Banco no encontrado'
        })
    
    informacion_bancos = {
        'Bancolombia': {
            'lecciones': [
                'Cuentas de Ahorro Básicas',
                'Creditos',
                'Préstamos Personales',
                'Seguros Básicos'
            ],
            'consejos': 'Ideal para comenzar tu vida financiera'
        },
        'BancoBogota': {
            'lecciones': [
            ],
            'consejos': ''
        },
        'Nequi': {
            'lecciones': [
            ],
            'consejos': ''
        },
        'banco4': {
            'lecciones': [
            ],
            'consejos': ''
        }
    }
    
    contexto = {
        'banco': banco_seleccionado,
        'info_adicional': informacion_bancos.get(banco_id, {
            'lecciones': ['Información en desarrollo...'],
            'consejos': 'Próximamente más información',
            'ventajas': ['Características en desarrollo']
        })
    }
    return render(request, 'banco_detalle.html', contexto)

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contexto = {'mensaje_exito': f'¡Gracias {nombre}! Te contactaremos pronto.'}
        return render(request, 'contacto.html', contexto)
    return render(request, 'contacto.html')
##formulario de satisfaccion 
def feedback(request):
    """Vista para quejas, reclamos y calificaciones"""
    if request.method == 'POST':
        # Procesar el formulario
        tipo = request.POST.get('tipo')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        calificacion = request.POST.get('calificacion')
        
        # Validar datos requeridos
        if not all([tipo, nombre, email, asunto, mensaje]):
            messages.error(request, 'Por favor completa todos los campos obligatorios.')
            return render(request, 'feedback.html')
        
        # Guardar en la base de datos
        feedback_obj = Feedback(
            tipo=tipo,
            nombre=nombre,
            email=email,
            asunto=asunto,
            mensaje=mensaje,
            calificacion=calificacion if calificacion else None
        )
        feedback_obj.save()
        
        # Mensaje de éxito
        if tipo == 'calificacion':
            messages.success(request, '¡Gracias por calificar nuestra aplicación!')
        else:
            messages.success(request, '¡Hemos recibido tu mensaje! Te contactaremos pronto.')
        
        return redirect('feedback')
    
    return render(request, 'feedback.html')

def gracias_feedback(request):
    """Página de agradecimiento después del feedback"""
    return render(request, 'gracias_feedback.html')