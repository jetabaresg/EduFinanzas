#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduFinanzas.settings')
django.setup()

from pagina_principal.models import Modulo, Contenido

print("=" * 60)
print("INSPECCIÓN DE BASE DE DATOS")
print("=" * 60)

total = Modulo.objects.count()
publicados = Modulo.objects.filter(publicado=True).count()

print(f"\nTotal de Módulos: {total}")
print(f"Módulos Publicados: {publicados}")

if Modulo.objects.exists():
    print("\nDetalle de módulos:")
    for m in Modulo.objects.all():
        contenidos = m.contenidos.count()
        print(f"  ID: {m.id}")
        print(f"    Título: {m.titulo}")
        print(f"    Publicado: {m.publicado}")
        print(f"    Contenidos: {contenidos}")
        print(f"    Orden: {m.orden}")
        print()
else:
    print("\n❌ NO HAY MÓDULOS EN LA BASE DE DATOS")
    print("\nProbables causas:")
    print("  1. La BD fue borrada o reseteada")
    print("  2. Las migraciones no se ejecutaron correctamente")
    print("  3. Los datos nunca fueron creados")
