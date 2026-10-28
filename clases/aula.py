"""Clase Aula (lugar físico donde se imparte un horario)."""
from base_datos.conexion import obtener_conexion


class Aula:
    def __init__(self, codigo_aula, capacidad=None, tipo=None, ubicacion=None):
        self._codigo_aula = codigo_aula
        self._capacidad = capacidad
        self._tipo = tipo
        self._ubicacion = ubicacion

    @property
    def datos(self):
        return {"codigo": self._codigo_aula, "capacidad": self._capacidad,
                "tipo": self._tipo, "ubicacion": self._ubicacion}

    def verificar_disponibilidad(self, dia, hora_inicio, hora_fin, excluir_id=None):
        """True si el aula está libre en ese día y rango de horas.
        'excluir_id' sirve al editar un horario para que no se compare contra sí mismo."""
        con = obtener_conexion()
        # Dos rangos se cruzan cuando: inicio_nuevo < fin_existente Y fin_nuevo > inicio_existente
        ocupadas = con.execute(
            "SELECT COUNT(*) FROM horarios WHERE codigo_aula = ? AND dia_semana = ? AND estado = 'Activo' "
            "AND hora_inicio < ? AND hora_fin > ? AND id_horario != ?",
            (self._codigo_aula, dia, hora_fin, hora_inicio, excluir_id or 0)).fetchone()[0]
        con.close()
        return ocupadas == 0

    @staticmethod
    def listar():
        con = obtener_conexion()
        filas = con.execute("SELECT * FROM aulas ORDER BY codigo_aula").fetchall()
        con.close()
        return [Aula(f["codigo_aula"], f["capacidad"], f["tipo"], f["ubicacion"]) for f in filas]
