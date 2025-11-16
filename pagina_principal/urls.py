from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),

    path('aprende/', views.aprende, name='aprende'),
    path('aprende/modulo/<int:modulo_id>/', views.detalle_modulo, name='detalle_modulo'),
    path('aprende/contenido/<int:contenido_id>/', views.ver_contenido, name='ver_contenido'),

    path('feedback/', views.feedback, name='feedback'),
]
