"""Clase Estudiante: rol extra pedido por el profesor. Hereda de Usuario."""
from clases.usuario import Usuario
from clases.horario import Horario


class Estudiante(Usuario):
    rol = "estudiante"

    def __init__(self, identificacion, nombres, apellidos, correo, clave, nivel):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel

    def consultar_horario(self):
        """El estudiante ve los horarios activos de las asignaturas de su nivel."""
        return Horario.listar_detallado("a.nivel = ? AND h.estado = 'Activo'", (self._nivel,))
