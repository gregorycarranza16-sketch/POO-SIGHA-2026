"""Clase Docente: hereda de Usuario."""
from clases.usuario import Usuario
from clases.horario import Horario
from base_datos.conexion import obtener_conexion


class Docente(Usuario):
    rol = "docente"

    def __init__(self, identificacion, nombres, apellidos, correo, clave, especialidad, max_horas_semanales):
        super().__init__(identificacion, nombres, apellidos, correo, clave)  # reutiliza el constructor del padre
        self._especialidad = especialidad
        self._max_horas_semanales = max_horas_semanales

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def max_horas_semanales(self):
        return self._max_horas_semanales

    def consultar_horario(self):
        """Horarios activos en los que este docente da clase."""
        return Horario.listar_detallado("h.docente_id = ? AND h.estado = 'Activo'", (self._identificacion,))

    @staticmethod
    def listar():
        """Lista de docentes (id + nombre) para el formulario del administrador."""
        con = obtener_conexion()
        filas = con.execute("SELECT id, nombres || ' ' || apellidos AS nombre FROM usuarios WHERE rol='docente'").fetchall()
        con.close()
        return [dict(f) for f in filas]
