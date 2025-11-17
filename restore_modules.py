#!/usr/bin/env python
"""
Script para restaurar módulos de ejemplo en la BD
Si los módulos fueron borrados, este script los recrea.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduFinanzas.settings')
django.setup()

from pagina_principal.models import Modulo, Contenido

print("=" * 70)
print("RESTAURANDO MÓDULOS DE EJEMPLO")
print("=" * 70)

# Eliminar módulos previos si existen (opcional)
Modulo.objects.all().delete()
print("✓ Base de datos limpia\n")

# Datos de módulos a restaurar
modulos_data = [
    {
        "titulo": "Introducción a las Finanzas Personales",
        "descripcion": "Aprende los conceptos básicos de finanzas personales y cómo manejar tu dinero de forma inteligente.",
        "orden": 1,
        "contenidos": [
            {"titulo": "¿Qué son las finanzas personales?", "tipo": "texto", "descripcion": "Concepto fundamental de finanzas personales"},
            {"titulo": "Principios básicos del dinero", "tipo": "video", "descripcion": "Video introductorio sobre dinero", "url_video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
            {"titulo": "Quiz: Conceptos Básicos", "tipo": "quiz", "descripcion": "Evalúa tu comprensión"},
        ]
    },
    {
        "titulo": "Presupuesto Personal",
        "descripcion": "Aprende a crear y mantener un presupuesto personal efectivo para controlar tus gastos.",
        "orden": 2,
        "contenidos": [
            {"titulo": "¿Cómo armar un presupuesto?", "tipo": "texto", "descripcion": "Guía paso a paso"},
            {"titulo": "Categorías de gastos", "tipo": "texto", "descripcion": "Tipos de gastos principales"},
            {"titulo": "Quiz: Tu Presupuesto", "tipo": "quiz", "descripcion": "Evalúa tu presupuesto"},
        ]
    },
    {
        "titulo": "Ahorro e Inversión",
        "descripcion": "Descubre estrategias para ahorrar dinero e invertir de forma segura para tu futuro.",
        "orden": 3,
        "contenidos": [
            {"titulo": "Importancia del ahorro", "tipo": "texto", "descripcion": "Por qué debes ahorrar"},
            {"titulo": "Métodos de ahorro", "tipo": "video", "descripcion": "Estrategias prácticas", "url_video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
            {"titulo": "Quiz: Ahorro e Inversión", "tipo": "quiz", "descripcion": "Evalúa tus conocimientos"},
        ]
    },
    {
        "titulo": "Control de Deuda",
        "descripcion": "Estrategias para gestionar y reducir deuda de forma efectiva.",
        "orden": 4,
        "contenidos": [
            {"titulo": "Tipos de deuda", "tipo": "texto", "descripcion": "Comprende la deuda"},
            {"titulo": "Plan de pago de deuda", "tipo": "texto", "descripcion": "Cómo liquidar deudas"},
            {"titulo": "Quiz: Gestión de Deuda", "tipo": "quiz", "descripcion": "Evalúa tu conocimiento"},
        ]
    },
    {
        "titulo": "Seguridad Financiera",
        "descripcion": "Aprende a proteger tu patrimonio y planificar para emergencias.",
        "orden": 5,
        "contenidos": [
            {"titulo": "Fondo de emergencia", "tipo": "texto", "descripcion": "Protección financiera"},
            {"titulo": "Seguros y protección", "tipo": "video", "descripcion": "Tipos de seguros", "url_video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
            {"titulo": "Quiz: Seguridad Financiera", "tipo": "quiz", "descripcion": "Evalúa tu comprensión"},
        ]
    },
]

# Crear módulos y contenidos
for mod_data in modulos_data:
    modulo = Modulo.objects.create(
        titulo=mod_data["titulo"],
        descripcion=mod_data["descripcion"],
        orden=mod_data["orden"],
        publicado=True
    )
    print(f"✓ Módulo creado: {modulo.titulo}")
    
    # Crear contenidos para este módulo
    for i, cont_data in enumerate(mod_data["contenidos"], 1):
        contenido = Contenido.objects.create(
            modulo=modulo,
            titulo=cont_data["titulo"],
            tipo=cont_data["tipo"],
            descripcion=cont_data.get("descripcion", ""),
            url_video=cont_data.get("url_video", ""),
            orden=i
        )
        print(f"  └─ Contenido: {contenido.titulo} ({contenido.tipo})")

print("\n" + "=" * 70)
print("✓ RESTAURACIÓN COMPLETADA")
print(f"  - Módulos creados: {Modulo.objects.count()}")
print(f"  - Contenidos creados: {Contenido.objects.count()}")
print("=" * 70)
