<h1><strong>EduFinanzas – Plataforma Educativa de Finanzas Personales</strong></h1>
<h1><strong>Jeronimo Tabares Gallego--Juan Manuel Lotero</strong></h1>
<p><strong>EduFinanzas</strong> es una aplicación web desarrollada en <strong>Django (Python)</strong> que permite a los usuarios aprender finanzas personales mediante módulos interactivos, simulaciones, evaluaciones y seguimiento de progreso. Incluye un panel administrativo para gestionar contenido, usuarios y estadísticas.</p>

<h2><strong>Características principales</strong></h2>

<h3><strong>Gestión de usuarios</strong></h3>
<ul>
    <li><strong>Registro e inicio de sesión</strong></li>
    <li><strong>Autenticación segura (Próximamente)</strong></li>
    <li><strong>Administración de usuarios (Próximamente)</strong></li>
</ul>

<h3><strong>Módulos educativos</strong></h3>
<ul>
    <li>Acceso a contenido educativo (videos, artículos, simulaciones)</li>
    <li>Navegación por módulos y recursos didácticos</li>
</ul>

<h3><strong>Simulaciones financieras (Próximamente)</strong></h3>
<ul>
    <li>Cálculo y análisis de escenarios financieros</li>
    <li>Generación de reportes </li>
</ul>

<h3><strong>Evaluaciones (Próximamente)</strong></h3>
<ul>
    <li>Preguntas por módulo</li>
    <li>Calificación automática</li>
    <li>Registro de puntajes</li>
</ul>

<h3><strong>Progreso del usuario </strong></h3>
<ul>
    <li>Visualización de avances y módulos completados </li>
    <li>Sincronización en la nube <li>(Próximamente)
</ul>

<h3><strong>Notificaciones (Próximamente)</strong></h3>
<ul>
    <li>Recordatorios de evaluaciones pendientes</li>
    <li>Avisos sobre nuevos módulos</li>
</ul>

<h3><strong>Panel administrativo (Próximamente)</strong></h3>
<ul>
    <li>Gestión de módulos y contenido</li>
    <li>Estadísticas del sistema</li>
</ul>

<h2><strong>Casos de uso</strong></h2>

<h3><strong>Realizados</strong></h3>
<table border="1" cellspacing="0" cellpadding="6">
    <tr>
        <th>ID</th>
        <th>Caso de uso</th>
        <th>Actor</th>
        <th>Descripción</th>
    </tr>
    <tr>
        <td><strong>CU-01</strong></td>
        <td>Registrarse / Iniciar sesión</td>
        <td>Usuario</td>
        <td>Permite autenticarse o crear cuenta nueva.</td>
    </tr>
    <tr>
        <td><strong>CU-02</strong></td>
        <td>Navegar módulos</td>
        <td>Usuario</td>
        <td>Accede al catálogo de módulos educativos.</td>
    </tr>
    <tr>
        <td><strong>CU-04</strong></td>
        <td>Acceder a contenido educativo</td>
        <td>Usuario</td>
        <td>Visualiza recursos del módulo seleccionado.</td>
    </tr>
    <tr><td><strong>CU-06</strong></td><td>Consultar progreso</td><td>Usuario</td><td>Consulta su avance y resultados.</td></tr>
</table>

<h3><strong>Pendientes</strong></h3>
<table border="1" cellspacing="0" cellpadding="6">
    <tr>
        <th>ID</th>
        <th>Caso de uso</th>
        <th>Actor</th>
        <th>Descripción</th>
    </tr>
    <tr><td><strong>CU-03</strong></td><td>Simulaciones financieras</td><td>Usuario registrado</td><td>Ejecuta ejercicios sobre ahorro, gasto o inversión.</td></tr>
    <tr><td><strong>CU-05</strong></td><td>Presentar evaluación</td><td>Usuario</td><td>Responde y envía la evaluación del módulo.</td></tr>
    <tr><td><strong>CU-07</strong></td><td>Recibir notificaciones</td><td>Usuario</td><td>Recibe alertas sobre actividades pendientes.</td></tr>
    <tr><td><strong>CU-08</strong></td><td>Sincronizar progreso</td><td>Usuario</td><td>Guarda avances entre dispositivos.</td></tr>
    <tr><td><strong>CU-09</strong></td><td>Administrar contenido</td><td>Administrador</td><td>Crear, editar y eliminar módulos.</td></tr>
    <tr><td><strong>CU-10</strong></td><td>Consultar estadísticas</td><td>Administrador</td><td>Muestra reportes del sistema.</td></tr>
    <tr><td><strong>CU-11</strong></td><td>Gestionar usuarios</td><td>Administrador</td><td>Crear, editar o eliminar cuentas.</td></tr>
</table>

<h2><strong>Tecnologías utilizadas</strong></h2>
<ul>
    <li>Python 3.x</li>
    <li>Django 4.x</li>
    <li>SQLite3</li>
    <li>HTML5, CSS3 y Bootstrap</li>
    <li>JavaScript</li>
</ul>

<h2><strong>Instalación y configuración</strong></h2>

<h3>1. Clonar el repositorio</h3>
<pre>git clone https://github.com/tu-usuario/EduFinanzas.git
cd EduFinanzas</pre>

<h3>2. Crear y activar un entorno virtual</h3>
<pre>python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate # Linux / Mac</pre>

<h3>3. Instalar dependencias</h3>
<pre>pip install -r requirements.txt</pre>

<h3>4. Realizar migraciones</h3>
<pre>python manage.py migrate</pre>

<h3>5. Ejecutar el servidor</h3>
<pre>python manage.py runserver</pre>

<p>La aplicación estará disponible en: <strong>http://127.0.0.1:8000/</strong></p>

