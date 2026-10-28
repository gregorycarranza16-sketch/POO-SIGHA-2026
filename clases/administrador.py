"""Clase Administrador: hereda de Usuario y gestiona los Horarios."""
from clases.usuario import Usuario
from clases.horario import Horario


class Administrador(Usuario):
    rol = "administrador"

    def __init__(self, identificacion, nombres, apellidos, correo, clave, cargo):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self._cargo = cargo

    @property
    def cargo(self):
        return self._cargo

    def crear_horario(self, asignatura, aula, docente_id, periodo, dia, hora_inicio, hora_fin):
        """Crea un horario. Devuelve (True/False, mensaje).
        (El diagrama solo muestra asignatura y aula; agregamos los demás datos porque un
        horario también necesita docente, período, día y horas.)"""
        if hora_inicio >= hora_fin:
            return False, "La hora de inicio debe ser menor que la hora de fin."
        nuevo = Horario(None, dia, hora_inicio, hora_fin, "Activo", docente_id, asignatura, aula, periodo)
        if nuevo.validar_cruce_horarios():
            return False, "Cruce de horarios: el docente o el aula ya están ocupados."
        nuevo.guardar()
        return True, "Horario creado correctamente."

    def modificar_horario(self, id_horario, dia, hora_inicio, hora_fin, estado):
        """Modifica día, horas y estado de un horario existente."""
        horario = Horario.buscar(id_horario)
        if horario is None:
            return False, "El horario no existe."
        if hora_inicio >= hora_fin:
            return False, "La hora de inicio debe ser menor que la hora de fin."
        # Para validar el cruce primero aplicamos los cambios al objeto (sin guardar aún)
        horario._dia_semana, horario._hora_inicio, horario._hora_fin = dia, hora_inicio, hora_fin
        if estado == "Activo" and horario.validar_cruce_horarios():
            return False, "Cruce de horarios: el docente o el aula ya están ocupados."
        horario.actualizar(dia, hora_inicio, hora_fin, estado)
        return True, "Horario modificado correctamente."
