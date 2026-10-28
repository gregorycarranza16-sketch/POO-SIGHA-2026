# Sistema web de gestión de horarios académicos

Proyecto universitario en Python (Flask + SQLite) basado en un diagrama de clases.
Tiene tres roles con inicio de sesión: **administrador**, **docente** y **estudiante**.

## 1. Cómo ejecutarlo

1. Instalar Python 3 desde python.org (en Windows, el instalador nuevo se llama "Python Install Manager").
2. Abrir esta carpeta (`proyecto_horarios`) en Visual Studio Code: *File → Open Folder*.
3. Abrir la terminal: *Terminal → New Terminal*.
4. Instalar Flask (solo la primera vez):
   ```
   python -m pip install flask
   ```
5. Ejecutar el proyecto:
   ```
   python main.py
   ```
6. Abrir en el navegador: **http://127.0.0.1:5000**
7. Para detenerlo: `Ctrl + C` en la terminal.

Para reiniciar los datos: detener el programa, borrar `base_datos/horarios.db` y volver a ejecutar `python main.py`.

## 2. Usuarios de prueba

| Rol | Correo | Clave |
|---|---|---|
| Administrador | admin@uni.edu | admin123 |
| Docente | docente@uni.edu (también maria@, jorge@, patricia@) | docente123 |
| Estudiante | estudiante@uni.edu (también diego@, valeria@) | estudiante123 |

## 3. Estructura del proyecto

```
proyecto_horarios/
├── main.py                  # punto de entrada: crea la BD y arranca Flask
├── clases/                  # una clase por archivo, según el diagrama
│   ├── __init__.py          # archivo principal: importa todas las clases
│   ├── usuario.py           # clase base
│   ├── docente.py           # hereda de Usuario
│   ├── estudiante.py        # hereda de Usuario (rol extra pedido por el profesor)
│   ├── administrador.py     # hereda de Usuario
│   ├── horario.py
│   ├── asignatura.py
│   ├── aula.py
│   └── periodo_academico.py
├── base_datos/
│   └── conexion.py          # conexión SQLite, creación de tablas y datos de ejemplo
└── interfaz/
    ├── app.py               # Flask: login, rutas y permisos por rol
    └── templates/           # páginas HTML (login y un panel por rol)
```

## 4. Resumen de las clases

- **Usuario** (base): identificación, nombres, apellidos, correo y clave. Métodos `iniciar_sesion()` y `cerrar_sesion()`.
- **Docente** (hereda de Usuario): especialidad y máximo de horas semanales. `consultar_horario()` muestra sus clases.
- **Estudiante** (hereda de Usuario): nivel. `consultar_horario()` muestra los horarios de su nivel.
- **Administrador** (hereda de Usuario): cargo. `crear_horario()` y `modificar_horario()`.
- **Horario**: día, hora de inicio y fin, estado. Se relaciona con un docente, una asignatura, un aula y un período. `validar_cruce_horarios()` y `mostrar_detalle()`.
- **Asignatura**: código, nombre, nivel y horas requeridas. `obtener_detalles()`.
- **Aula**: código, capacidad, tipo y ubicación. `verificar_disponibilidad()`.
- **PeriodoAcademico**: código, fechas y estado. Contiene muchos horarios. `activar_periodo()` y `finalizar_periodo()`.

## 5. Cómo funciona

- **Herencia:** Docente, Estudiante y Administrador heredan de Usuario con `super().__init__()`.
- **Login:** `app.py` busca al usuario por correo y llama a `iniciar_sesion()`. Las claves se guardan cifradas (hash), nunca en texto plano.
- **Roles:** el decorador `rol_requerido` deja entrar a cada panel solo al rol correcto.
- **Base de datos:** SQLite (un solo archivo, sin instalar nada). Los cuatro tipos de usuario comparten la tabla `usuarios` con una columna `rol`; `usuario_desde_fila()` crea el objeto de la clase correcta.
- **Cruces de horarios:** al crear o editar un horario se comprueba que el docente y el aula no estén ocupados en ese día y rango de horas.

## 6. Diferencias con el diagrama (por si preguntan)

- Se agregó la clase **Estudiante**, pedida aparte por el profesor.
- `crear_horario()` recibe más parámetros que `(asignatura, aula)`, porque un horario también necesita docente, período, día y horas.
- Se añadieron métodos auxiliares (`guardar()`, `buscar()`, `listar()`) para trabajar con la base de datos.

# usuarios de prueba 
Rol	Correo	Clave
Administrador:	admin@uni.edu	:admin123
Docente:	docente@uni.edu	:docente123
Estudiante:	estudiante@uni.edu	:estudiante123