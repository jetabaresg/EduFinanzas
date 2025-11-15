from django.urls import path
from . import views

app_name = 'usuarios'   # ← ESTO ES OBLIGATORIO

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registrarse, name='registro'),
]
