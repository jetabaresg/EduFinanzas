from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('aprende/', views.aprende, name='aprende'),
    path('aprende/<str:banco_id>/', views.banco_detalle, name='banco_detalle'),
    path('feedback/', views.feedback, name='feedback'),  
    path('gracias-feedback/', views.gracias_feedback, name='gracias_feedback'), 
]