"""Archivo principal del paquete 'clases': importa todas las clases juntas, así desde
otras carpetas basta con:  from clases import Docente, Horario, ...
También tiene la 'fábrica' que convierte una fila de la BD en el objeto correcto."""
from base_datos.conexion import obtener_conexion
from clases.usuario import Usuario
from clases.docente import Docente
from clases.estudiante import Estudiante
from clases.administrador import Administrador
from clases.asignatura import Asignatura
from clases.aula import Aula
from clases.periodo_academico import PeriodoAcademico
from clases.horario import Horario, DIAS


def usuario_desde_fila(f):
    """Según la columna 'rol' crea un Docente, Estudiante o Administrador (polimorfismo)."""
    if f is None:
        return None
    base = (f["id"], f["nombres"], f["apellidos"], f["correo"], f["clave"])
    if f["rol"] == "docente":
        return Docente(*base, f["especialidad"], f["max_horas_semanales"])
    if f["rol"] == "estudiante":
        return Estudiante(*base, f["nivel"])
    return Administrador(*base, f["cargo"])


def buscar_usuario_por_correo(correo):
    con = obtener_conexion()
    fila = con.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,)).fetchone()
    con.close()
    return usuario_desde_fila(fila)


def buscar_usuario_por_id(id_usuario):
    con = obtener_conexion()
    fila = con.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,)).fetchone()
    con.close()
    return usuario_desde_fila(fila)
