EduFinanzas – Plataforma Educativa de Finanzas Personales

EduFinanzas es una aplicación web desarrollada en Django (Python) que permite a usuarios aprender finanzas personales mediante módulos interactivos, simulaciones, evaluaciones y seguimiento de progreso.
Incluye además un panel administrativo para gestión de contenido, usuarios y estadísticas del sistema.

Características principales
Gestión de usuarios

Registro e inicio de sesión.

Autenticación segura.

Administración de usuarios para perfiles administradores.(Proximamente)

Módulos educativos

Acceso a contenido educativo (videos, artículos, simulaciones).

Navegación por módulos y recursos didácticos.

Simulaciones financieras(Proximamente)

Cálculo y análisis de escenarios financieros (ahorro, inversión, presupuesto).

Generación de reportes.(Proximamente)

Evaluaciones

Preguntas por módulo.

Calificación automática.

Registro de puntajes.

Progreso del usuario

Visualización de avances, calificaciones y módulos completados.

Sincronización en la nube (si hay conexión).(Proximamente)

Notificaciones(Proximamente)

Recordatorios de evaluaciones pendientes.(Proximamente)

Avisos sobre nuevos módulos.(Proximamente)

Panel administrativo(Proximamente)

Gestión de módulos y contenido educativo.(Proximamente)

Estadísticas de uso del sistema.(Proximamente)

Casos de uso 

Los principales casos de uso implementados en EduFinanzas son:

ID	Caso de uso	Actor principal	Descripción
Realizados
CU-01	Registrarse / Iniciar sesión	Usuario	Permite al usuario autenticarse o crear cuenta nueva.
CU-02	Navegar módulos	Usuario	Accede al catálogo de módulos educativos.
CU-04	Acceder a contenido educativo	Usuario	Visualiza recursos del módulo seleccionado.
Pendientes
CU-03	Simulaciones financieras	Usuario registrado	Ejecuta ejercicios sobre ahorro, gasto o inversión.
CU-05	Presentar evaluación	Usuario	Responde y envía la evaluación del módulo.
CU-06	Consultar progreso	Usuario	Consulta su avance y resultados.
CU-07	Recibir notificaciones	Usuario	Recibe alertas sobre actividades pendientes.
CU-08	Sincronizar progreso en la nube	Usuario	Guarda avances entre dispositivos.
CU-09	Administrar contenido	Administrador	Permite crear/editar/eliminar módulos y recursos.
CU-10	Consultar estadísticas	Administrador	Muestra reportes del uso del sistema.
CU-11	Gestionar usuarios	Administrador	Crea, edita o elimina cuentas.

Tecnologías utilizadas

Python 3.x

Django 4.x

SQLite3 (base de datos por defecto)

HTML5, CSS3 y Bootstrap

JavaScript

Instalación y configuración
1️⃣ Clonar el repositorio
git clone https://github.com/tu-usuario/EduFinanzas.git
cd EduFinanzas

2️⃣ Crear y activar un entorno virtual
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate # Linux / Mac

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Realizar migraciones
python manage.py migrate

5️⃣ Ejecutar el servidor de desarrollo
python manage.py runserver

La aplicación estará disponible en:

http://127.0.0.1:8000/

