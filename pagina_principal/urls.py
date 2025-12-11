from django.urls import path
from . import views
# ---------------------------
# ADMINISTRACIÓN DE CONTENIDO
# ---------------------------
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),

    path('aprende/', views.aprende, name='aprende'),
    path('aprende/modulo/<int:modulo_id>/', views.detalle_modulo, name='detalle_modulo'),
    path('aprende/contenido/<int:contenido_id>/', views.ver_contenido, name='ver_contenido'),
    path('evaluacion/<int:contenido_id>/procesar/', views.procesar_evaluacion, name='procesar_evaluacion'),
    path('evaluacion/intento/<int:intento_id>/abandonar/', views.abandonar_evaluacion, name='abandonar_evaluacion'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('progreso/', views.ver_progreso, name='ver_progreso'),
    path('feedback/', views.feedback, name='feedback'),
      # Módulos
    path('admin_contenido/modulos/', staff_member_required(views.admin_modulos_lista), name='admin_modulos_lista'),
    path('admin_contenido/modulos/crear/', staff_member_required(views.admin_modulo_crear), name='admin_modulo_crear'),
    path('admin_contenido/modulos/editar/<int:modulo_id>/', staff_member_required(views.admin_modulo_editar), name='admin_modulo_editar'),
    path('admin_contenido/modulos/eliminar/<int:modulo_id>/', staff_member_required(views.admin_modulo_eliminar), name='admin_modulo_eliminar'),

    # Contenidos
    path('admin_contenido/modulos/<int:modulo_id>/contenidos/', staff_member_required(views.admin_contenidos_lista), name='admin_contenidos_lista'),
    path('admin_contenido/contenidos/crear/<int:modulo_id>/', staff_member_required(views.admin_contenido_crear), name='admin_contenido_crear'),
    path('admin_contenido/contenidos/editar/<int:contenido_id>/', staff_member_required(views.admin_contenido_editar), name='admin_contenido_editar'),
    path('admin_contenido/contenidos/eliminar/<int:contenido_id>/', staff_member_required(views.admin_contenido_eliminar), name='admin_contenido_eliminar'),
]


