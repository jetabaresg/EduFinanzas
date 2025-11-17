#!/usr/bin/env python
"""
Script para restaurar módulos con contenido extendido y evaluaciones simples.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduFinanzas.settings')
django.setup()

from pagina_principal.models import Modulo, Contenido, Pregunta, OpcionRespuesta

print("=" * 90)
print("RESTAURANDO MÓDULOS CON CONTENIDO EXTENDIDO Y EVALUACIONES")
print("=" * 90)

# Borrar datos previos
Modulo.objects.all().delete()
print("✓ Base de datos limpia\n")

# DATOS CON DESCRIPCIONES EXTENDIDAS
modulos_data = [
    {
        "titulo": "Fundamentos de Finanzas Personales",
        "descripcion": "Aprende los conceptos básicos de finanzas personales, ingresos, egresos y decisiones financieras inteligentes. Este módulo te introduce en el mundo de las finanzas personales, enseñándote los principios fundamentales para tomar mejores decisiones con tu dinero y construir una base sólida para tu futuro financiero.",
        "orden": 1,
        "contenidos": [
            {
                "titulo": "¿Qué son las Finanzas Personales?",
                "tipo": "texto",
                "descripcion": "Las finanzas personales son la rama de la economía que se encarga del manejo del dinero en la vida cotidiana. Incluye decisiones sobre ingresos, gastos, ahorros, deudas e inversiones. El objetivo es optimizar el uso de recursos para lograr seguridad financiera y bienestar económico a largo plazo.\n\n¿Por qué son importantes? Porque cada día tomamos decisiones financieras: qué comer, dónde vivir, si estudiar, si invertir. Sin un conocimiento básico de finanzas, estas decisiones pueden ser perjudiciales para nuestro futuro. Las finanzas personales te ayudan a:\n\n1. Entender de dónde viene tu dinero (ingresos)\n2. Saber a dónde va tu dinero (gastos)\n3. Tomar decisiones inteligentes sobre endeudamiento\n4. Construir riqueza a través del ahorro e inversión\n5. Protegerte a ti y a tu familia ante imprevistos\n\nLa buena noticia es que no necesitas ser un experto en matemáticas o economía para dominar las finanzas personales. Solo necesitas disciplina, educación y la voluntad de mejorar tu situación financiera.",
            },
            {
                "titulo": "Los Pilares Fundamentales de la Educación Financiera",
                "tipo": "video",
                "descripcion": "Video educativo que explica los 4 pilares fundamentales: 1) Ingresos - fuentes de dinero, 2) Gastos - dónde va el dinero, 3) Ahorro - guardar para el futuro, 4) Inversión - hacer que el dinero trabaje.",
                "url_video": "https://www.youtube.com/watch?v=9sCVcWD1Svs",
                "preguntas": [
                    {
                        "texto": "¿Cuáles son los 4 pilares fundamentales de la educación financiera?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Ingresos, Gastos, Ahorro, Inversión", "correcta": True},
                            {"texto": "Ingresos, Endeudamiento, Ahorro, Gasto", "correcta": False},
                            {"texto": "Trabajo, Dinero, Banco, Tarjeta", "correcta": False},
                            {"texto": "Salario, Hipoteca, Fondo, Acciones", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Qué es un ingreso?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "El dinero que entra a tu cuenta (salario, rentas, etc)", "correcta": True},
                            {"texto": "El dinero que gastas en comer", "correcta": False},
                            {"texto": "El dinero que depositas en el banco", "correcta": False},
                            {"texto": "El dinero que deben pagarte", "correcta": False},
                        ]
                    }
                ]
            },
            {
                "titulo": "Evaluación: Conceptos Básicos de Finanzas",
                "tipo": "quiz",
                "descripcion": "Responde preguntas sobre conceptos fundamentales: definición de finanzas personales, tipos de ingresos, clasificación de gastos y diferencia entre ahorro e inversión.",
                "preguntas": [
                    {
                        "texto": "¿Cuál es el objetivo principal de las finanzas personales?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Optimizar el uso de recursos para lograr seguridad financiera", "correcta": True},
                            {"texto": "Gastar todo el dinero que tenemos", "correcta": False},
                            {"texto": "Endeudarse lo máximo posible", "correcta": False},
                            {"texto": "No pensar en el dinero", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Qué son los gastos fijos?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Gastos que se repiten todos los meses (arriendo, servicios, etc)", "correcta": True},
                            {"texto": "Gastos que realizas una sola vez", "correcta": False},
                            {"texto": "Dinero que ahorras cada mes", "correcta": False},
                            {"texto": "Dinero que inviertes en acciones", "correcta": False},
                        ]
                    }
                ]
            },
        ]
    },
    {
        "titulo": "Presupuesto Personal: Control Total de tu Dinero",
        "descripcion": "Domina la técnica del presupuesto para controlar tus ingresos, gastos y alcanzar tus metas financieras. Un presupuesto es tu mapa financiero: te muestra exactamente dónde está tu dinero y te ayuda a tomar decisiones conscientes. Sin presupuesto, es fácil gastar dinero sin saber en qué, terminar con deudas inesperadas y perder oportunidades de ahorro.",
        "orden": 2,
        "contenidos": [
            {
                "titulo": "Cómo Crear tu Primer Presupuesto",
                "tipo": "texto",
                "descripcion": "Un presupuesto es un plan detallado de tus ingresos y gastos.\n\nPasos para crear tu presupuesto:\n\n1. **Calcula tus ingresos mensuales**: Suma todo lo que entra: salario, rentas, freelance, negocio propio, etc. Sé realista y usa números netos (después de impuestos).\n\n2. **Enumera todos tus gastos fijos**: Estos no cambian cada mes. Ejemplos: arriendo ($800), servicios ($150), internet ($50), seguros ($100). Total: $1100.\n\n3. **Suma gastos variables**: Estos cambian cada mes. Ejemplos: comida ($400), transporte ($100), entretenimiento ($150). Total: $650.\n\n4. **Compara ingresos vs gastos**: Si ingresos ($2500) > gastos ($1750), tienes un excedente de $750. Este dinero debe ir a ahorros e inversiones. Si gastos > ingresos, necesitas reducir gastos o aumentar ingresos.\n\n5. **Ajusta según sea necesario**: Un presupuesto realista es flexible. Si falta dinero para algo importante, reduce gastos no esenciales.\n\n**Herramientas útiles**: Excel, Google Sheets, apps como YNAB, PocketGuard, o Mint. Elige la que te sea más cómoda.\n\n**Principio clave**: Un buen presupuesto no es restrictivo, es liberador. Te da control sobre tu dinero en lugar de que el dinero te controle a ti.",
            },
            {
                "titulo": "Método 50/30/20: La Regla de Oro del Presupuesto",
                "tipo": "video",
                "descripcion": "Aprende la regla más popular y efectiva: destina 50% de ingresos a necesidades (alimento, vivienda, utilidades), 30% a deseos (entretenimiento, vacaciones), 20% a ahorros e inversiones. Estos porcentajes pueden ajustarse según tu situación personal.",
                "url_video": "https://www.youtube.com/watch?v=_bgUUswBttU",
                "preguntas": [
                    {
                        "texto": "En la regla 50/30/20, ¿qué porcentaje se destina a necesidades?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "50%", "correcta": True},
                            {"texto": "30%", "correcta": False},
                            {"texto": "20%", "correcta": False},
                            {"texto": "40%", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Cuáles son ejemplos de necesidades en la regla 50/30/20?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Alimento, vivienda, servicios básicos", "correcta": True},
                            {"texto": "Películas, viajes, ropa de marca", "correcta": False},
                            {"texto": "Acciones, fondos, inversiones", "correcta": False},
                            {"texto": "Tarjetas de crédito, deudas", "correcta": False},
                        ]
                    }
                ]
            },
            {
                "titulo": "Evaluación: Presupuesto y Control de Gastos",
                "tipo": "quiz",
                "descripcion": "Ejercicios prácticos: calcula presupuestos, identifica gastos innecesarios, aplica la regla 50/30/20.",
                "preguntas": [
                    {
                        "texto": "Si tus ingresos mensuales son $3000 y aplicando 50/30/20 ¿cuánto debes destinar a ahorros?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "$600", "correcta": True},
                            {"texto": "$1500", "correcta": False},
                            {"texto": "$900", "correcta": False},
                            {"texto": "$300", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Cuál es el primer paso para crear un presupuesto?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Calcular tus ingresos mensuales", "correcta": True},
                            {"texto": "Gastar todo tu dinero", "correcta": False},
                            {"texto": "Abrir una tarjeta de crédito", "correcta": False},
                            {"texto": "Invertir en la bolsa", "correcta": False},
                        ]
                    }
                ]
            },
        ]
    },
    {
        "titulo": "Ahorro e Inversión: Haz que tu Dinero Trabaje",
        "descripcion": "Descubre estrategias de ahorro y cómo iniciar en el mundo de las inversiones para multiplicar tu patrimonio. La diferencia entre personas ricas y pobres no es solo cuánto ganan, sino cuánto ahorran e invierten. Aprenderás que el dinero puede trabajar para ti generando dinero adicional.",
        "orden": 3,
        "contenidos": [
            {
                "titulo": "La Importancia Crucial del Ahorro",
                "tipo": "texto",
                "descripcion": "Ahorrar significa guardar dinero para el futuro en lugar de gastarlo todo hoy.\n\n**¿Por qué es importante ahorrar?**\n\n1. **Seguridad ante emergencias**: Una reparación del auto, enfermedad, desempleo. Sin ahorros, estas emergencias se vuelven créditos costosos.\n\n2. **Libertad y poder**: Dinero ahorrado = opciones. Puedes cambiar de trabajo, empezar un negocio, tomarte un descanso sin estrés.\n\n3. **Logro de metas**: Vacaciones, educación, casa, auto. Requieren ahorro sostenido.\n\n4. **Reducción de estrés**: Estudios muestran que tener ahorros reduce ansiedad y mejora salud mental.\n\n5. **Base para inversión**: No puedes invertir sin ahorros. Los ahorros son la semilla del crecimiento financiero.\n\n**Meta inicial: Fondo de emergencia de 3-6 meses de gastos**\n\nSi gastas $1500/mes, tu objetivo es $4500-$9000. ¿Parece mucho? Comienza pequeño:\n\n- Mes 1-3: Ahorra $100/mes = $300\n- Mes 4-6: Aumenta a $200/mes = $600\n- Total después de 6 meses: $900\n\nEs progreso. Después, invierte el ahorro extra.\n\n**Estrategias de ahorro:**\n\n1. **Ahorro automático**: Configura una transferencia el mismo día que recibes tu salario. Si no ves el dinero, no lo gastas.\n\n2. **Cuenta separada**: Abre una cuenta de ahorro diferente a tu cuenta principal. Psicológicamente, es más difícil gastar dinero que está \"en otro lado\".\n\n3. **Apps de ahorro**: Muchas redondean compras y ahorran la diferencia (ej: $3.50 → $4.00, ahorra $0.50).\n\n4. **Desafío 30 días**: No gastes en lujos durante 30 días. Verás cuánto dinero tienes de repente.",
            },
            {
                "titulo": "Introducción a la Inversión para Principiantes",
                "tipo": "video",
                "descripcion": "Video explicativo sobre tipos de inversión accesibles: 1) Cuentas de ahorro de alto rendimiento, 2) Certificados de depósito (CDT), 3) Fondos mutuos, 4) Acciones, 5) Bienes raíces.",
                "url_video": "https://www.youtube.com/watch?v=9xW0HK7IUo0",
                "preguntas": [
                    {
                        "texto": "¿Cuál es la diferencia principal entre ahorro e inversión?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "La inversión busca multiplicar dinero, el ahorro solo guardarlo", "correcta": True},
                            {"texto": "No hay diferencia", "correcta": False},
                            {"texto": "El ahorro es más rentable", "correcta": False},
                            {"texto": "La inversión es más segura", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Cuál es una ventaja de invertir en fondos mutuos?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Diversificación sin necesidad de ser experto", "correcta": True},
                            {"texto": "Garantía de ganancia", "correcta": False},
                            {"texto": "No hay riesgo", "correcta": False},
                            {"texto": "Liquidez inmediata", "correcta": False},
                        ]
                    }
                ]
            },
            {
                "titulo": "Evaluación: Ahorro e Inversión",
                "tipo": "quiz",
                "descripcion": "Preguntas sobre diferencia entre ahorro e inversión, tipos de inversiones, rentabilidad y riesgo.",
                "preguntas": [
                    {
                        "texto": "¿Cuántos meses de gastos debe tener un fondo de emergencia recomendado?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "3 a 6 meses", "correcta": True},
                            {"texto": "1 a 2 meses", "correcta": False},
                            {"texto": "12 meses", "correcta": False},
                            {"texto": "6 meses es siempre obligatorio", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Cuál es la mejor estrategia para comenzar a ahorrar?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Ahorro automático el día que recibes tu salario", "correcta": True},
                            {"texto": "Ahorrar lo que sobre al final del mes", "correcta": False},
                            {"texto": "Guardar dinero debajo del colchón", "correcta": False},
                            {"texto": "No es posible ahorrar con un salario bajo", "correcta": False},
                        ]
                    }
                ]
            },
        ]
    },
    {
        "titulo": "Gestión Inteligente de la Deuda",
        "descripcion": "Entiende los tipos de deuda, tasas de interés y estrategias efectivas para eliminar deuda y mejorar tu salud financiera. No toda deuda es mala, pero la deuda mal manejada puede arruinarte financieramente. Aprenderás a distinguir deuda buena de deuda mala y cómo salir de deudas rápidamente.",
        "orden": 4,
        "contenidos": [
            {
                "titulo": "Tipos de Deuda: Buena vs Mala",
                "tipo": "texto",
                "descripcion": "Existen dos tipos de deuda: buena y mala.\n\n**DEUDA BUENA**\n\nEs inversión en tu futuro. Generas ingresos después gracias a la deuda.\n\nEjemplos:\n- **Crédito educativo**: Pagas $20,000 por una carrera que te permite ganar $40,000/año más. ROI positivo.\n- **Hipoteca**: Compras casa a $150,000. Después vale $200,000. Además, pagarías arriendo igualmente.\n- **Crédito para negocio**: Pides $10,000 y generas $50,000 en ganancias.\n\nCaracterísticas: Bajo interés, largo plazo, generan ingresos futuros.\n\n**DEUDA MALA**\n\nEs consumo de cosas que se deprecian. Pagas más de lo que compraste.\n\nEjemplos:\n- **Tarjeta de crédito en consumo**: Compras ropa por $500 a 24% anual. Terminas pagando $650.\n- **Crédito para auto lujoso**: Auto de $40,000 se deprecia a $25,000 en 3 años. Pagaste $50,000 en total (con intereses).\n- **Payday loans**: Pequeños créditos a tasas de 400% anual. Es usura.\n\nCaracterísticas: Alto interés, corto plazo, dinero se va en consumo.\n\n**CONCEPTO CLAVE: TASA DE INTERÉS**\n\nEs el porcentaje que pagas por dinero prestado, generalmente anual.\n\nEjemplo: Deuda de $1000 a 5% anual\n- Pagas $50 en intereses al año\n- Deuda total: $1050\n\nMismo $1000 a 25% anual\n- Pagas $250 en intereses al año\n- Deuda total: $1250\n\n¿Ves la diferencia? Tasas altas te roban dinero.\n\n**IMPACTO EN LARGO PLAZO**\n\nUna deuda de $10,000 a 5% vs 25% anual:\n- Al 5%: Pagas ~$1300 en intereses en 3 años\n- Al 25%: Pagas ~$5500 en intereses en 3 años\n\nLa diferencia es $4200. Ese dinero podría estar en tu bolsillo.",
            },
            {
                "titulo": "Estrategias Probadas para Eliminar Deuda",
                "tipo": "video",
                "descripcion": "Dos métodos efectivos: MÉTODO BOLA DE NIEVE y MÉTODO AVALANCHA. Tips para eliminar deuda rápidamente.",
                "url_video": "https://www.youtube.com/watch?v=A6H5t7GJnOw",
                "preguntas": [
                    {
                        "texto": "¿Cuál es la estrategia del 'Método Bola de Nieve'?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Pagar primero las deudas pequeñas para ganar momentum", "correcta": True},
                            {"texto": "Pagar primero las deudas con tasa más alta", "correcta": False},
                            {"texto": "No pagar las deudas", "correcta": False},
                            {"texto": "Consolidar todas las deudas en una", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Cuál es la ventaja psicológica del Método Bola de Nieve?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Ganas momentum viendo deudas desaparecer", "correcta": True},
                            {"texto": "Ahorras más en intereses", "correcta": False},
                            {"texto": "Es la única estrategia posible", "correcta": False},
                            {"texto": "No hay ventaja", "correcta": False},
                        ]
                    }
                ]
            },
            {
                "titulo": "Evaluación: Gestión de Deuda",
                "tipo": "quiz",
                "descripcion": "Casos prácticos: clasifica deudas buenas/malas, calcula intereses.",
                "preguntas": [
                    {
                        "texto": "¿Cuál es un ejemplo de deuda BUENA?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Crédito educativo para una carrera", "correcta": True},
                            {"texto": "Tarjeta de crédito en consumo", "correcta": False},
                            {"texto": "Payday loan", "correcta": False},
                            {"texto": "Crédito rápido sin verificación", "correcta": False},
                        ]
                    },
                    {
                        "texto": "Si tienes deudas con tasas de 5%, 10% y 25%, ¿cuál deberías pagar primero si usas Método Avalancha?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "La deuda al 25% porque cuesta más en intereses", "correcta": True},
                            {"texto": "La deuda al 5% porque es la más pequeña", "correcta": False},
                            {"texto": "Todas por igual", "correcta": False},
                            {"texto": "Ninguna, ignorar deudas", "correcta": False},
                        ]
                    }
                ]
            },
        ]
    },
    {
        "titulo": "Planificación Financiera a Largo Plazo: Tu Futuro Asegurado",
        "descripcion": "Planifica tu futuro financiero: retiro cómodo, protección familiar mediante seguros y construcción sostenida de patrimonio. La diferencia entre quienes terminan con seguridad financiera y quienes no, es la planificación. Los ricos no son más inteligentes, simplemente piensan a largo plazo.",
        "orden": 5,
        "contenidos": [
            {
                "titulo": "Fondo de Emergencia: Tu Red de Seguridad Financiera",
                "tipo": "texto",
                "descripcion": "El fondo de emergencia es dinero guardado y accesible para imprevistos.\n\n**EMERGENCIAS TÍPICAS**\n\n1. **Desempleo**: Pierdes tu trabajo. Tienes 3-6 meses antes de crisis financiera.\n2. **Enfermedad**: Gastos médicos inesperados, medicinas, cirugía.\n3. **Reparaciones urgentes**: Auto necesita reparación ($2000), techo con filtraciones ($5000).\n4. **Emergencias familiares**: Funeral, ayuda a familiares, crianza de nietos.\n5. **Pérdida de ingresos**: Cliente importante desaparece, negocio va mal.\n\n**RECOMENDACIÓN ESTÁNDAR: 3-6 MESES DE GASTOS TOTALES**\n\n¿Por qué 3-6?\n- 3 meses: Mínimo razonable, tiempo para encontrar empleo\n- 6 meses: Ideal si tienes dependientes o trabajo inestable\n- Más de 6 meses: Dinero que debería estar invertido\n\n**CÁLCULO PRÁCTICO**\n\nSi tus gastos mensuales son:\n- Arriendo: $800\n- Comida: $400\n- Servicios: $150\n- Transporte: $100\n- **Total: $1450**\n\nTu fondo de emergencia objetivo es:\n- Mínimo (3 meses): $1450 × 3 = $4350\n- Ideal (6 meses): $1450 × 6 = $8700\n\n**UBICACIÓN DEL FONDO**\n\nNO está en:\n- ❌ Debajo del colchón (inflación lo come)\n- ❌ Tarjeta de crédito (podrías no poder acceder)\n- ❌ Plazo fijo que requiere retiro anticipado penalizado\n\nESTÁ en:\n- ✅ Cuenta de ahorros de fácil acceso\n- ✅ Cuenta de ahorro de alto rendimiento (4-5% anual)\n- ✅ Fondos de dinero del mercado (bajo riesgo)\n\n**CÓMO CONSTRUIR EL FONDO**\n\nNo tienes que hacerlo en 6 meses. Pueden ser años:\n\n- **Meta agresiva**: 10% de ingresos/mes → $200 de $2000 → Fondo de $1450 en 7-8 meses\n- **Meta moderada**: 5% de ingresos/mes → $100 de $2000 → Fondo de $1450 en 14-15 meses\n- **Meta conservadora**: 2% de ingresos/mes → $40 de $2000 → Fondo de $1450 en 3+ años\n\nLo importante es COMENZAR. Incluso $50/mes suma rápido.\n\n**PROTECCIÓN DEL FONDO**\n\nUna vez construido:\n- Úsalo SOLO para emergencias reales\n- Si lo gastas, reconstruye pronto\n- Incrementa cuando tus gastos suben\n- Mantén en lugar seguro, accesible pero no muy fácil de tocar",
            },
            {
                "titulo": "Seguros y Protección del Patrimonio",
                "tipo": "video",
                "descripcion": "TIPOS DE SEGUROS: Seguro de vida, salud, hogar, auto. IMPORTANCIA y cálculos.",
                "url_video": "https://www.youtube.com/watch?v=IMxIeV3YKLA",
                "preguntas": [
                    {
                        "texto": "¿Cuál es la función principal del seguro de vida?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Proteger financieramente a la familia si falleces", "correcta": True},
                            {"texto": "Hacerse rico rápido", "correcta": False},
                            {"texto": "Evitar gastos médicos", "correcta": False},
                            {"texto": "Invertir dinero en bolsa", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Cuál debería ser la cobertura de seguro de vida según expertos?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "10 veces tu ingreso anual", "correcta": True},
                            {"texto": "1 año de ingreso", "correcta": False},
                            {"texto": "Lo que puedas pagar", "correcta": False},
                            {"texto": "No se necesita seguro de vida", "correcta": False},
                        ]
                    }
                ]
            },
            {
                "titulo": "Evaluación: Planificación Financiera a Largo Plazo",
                "tipo": "quiz",
                "descripcion": "Calcula fondo de emergencia necesario, elige seguros apropiados.",
                "preguntas": [
                    {
                        "texto": "Si gastas $2000/mes, ¿cuál debería ser tu fondo de emergencia ideal (6 meses)?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "$12,000", "correcta": True},
                            {"texto": "$6,000", "correcta": False},
                            {"texto": "$24,000", "correcta": False},
                            {"texto": "$2,000", "correcta": False},
                        ]
                    },
                    {
                        "texto": "¿Qué es lo más importante en planificación financiera a largo plazo?",
                        "tipo": "opcion_multiple",
                        "opciones": [
                            {"texto": "Pensar en el futuro y tomar acciones hoy", "correcta": True},
                            {"texto": "Ser rico desde ahora", "correcta": False},
                            {"texto": "No gastar dinero nunca", "correcta": False},
                            {"texto": "Invertir en lotería", "correcta": False},
                        ]
                    }
                ]
            },
        ]
    },
]

# Crear módulos, contenidos y preguntas
for mod_data in modulos_data:
    modulo = Modulo.objects.create(
        titulo=mod_data["titulo"],
        descripcion=mod_data["descripcion"],
        orden=mod_data["orden"],
        publicado=True
    )
    print(f"✓ Módulo {modulo.orden}: {modulo.titulo}")
    
    for idx, cont_data in enumerate(mod_data["contenidos"], 1):
        contenido = Contenido.objects.create(
            modulo=modulo,
            titulo=cont_data["titulo"],
            tipo=cont_data["tipo"],
            descripcion=cont_data.get("descripcion", ""),
            url_video=cont_data.get("url_video", ""),
            orden=idx
        )
        
        # Crear preguntas si existen
        if "preguntas" in cont_data:
            for p_idx, pregunta_data in enumerate(cont_data["preguntas"], 1):
                pregunta = Pregunta.objects.create(
                    contenido=contenido,
                    texto=pregunta_data["texto"],
                    tipo=pregunta_data["tipo"],
                    orden=p_idx,
                    puntos=1
                )
                
                # Crear opciones de respuesta
                for o_idx, opcion_data in enumerate(pregunta_data["opciones"], 1):
                    OpcionRespuesta.objects.create(
                        pregunta=pregunta,
                        texto=opcion_data["texto"],
                        es_correcta=opcion_data["correcta"],
                        orden=o_idx
                    )
        
        print(f"  └─ [{idx}] {contenido.titulo} ({contenido.tipo})")

print("\n" + "=" * 90)
print("✓ RESTAURACIÓN COMPLETADA CON ÉXITO")
print(f"  - Módulos: {Modulo.objects.count()}")
print(f"  - Contenidos: {Contenido.objects.count()}")
print(f"  - Preguntas: {Pregunta.objects.count()}")
print("=" * 90)
print("\nSiguiente paso: Accede a http://127.0.0.1:8000/aprende/ para ver los módulos")
print("               con contenido EXTENDIDO y EVALUACIONES SIMPLES")
