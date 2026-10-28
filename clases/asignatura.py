"""Clase Asignatura (materia que se dicta en un horario)."""
from base_datos.conexion import obtener_conexion


class Asignatura:
    def __init__(self, codigo_asignatura, nombre, nivel, horas_requeridas):
        self._codigo_asignatura = codigo_asignatura
        self._nombre = nombre
        self._nivel = nivel
        self._horas_requeridas = horas_requeridas

    def obtener_detalles(self):
        """Devuelve los datos de la asignatura en un diccionario."""
        return {"codigo": self._codigo_asignatura, "nombre": self._nombre,
                "nivel": self._nivel, "horas": self._horas_requeridas}

    @staticmethod
    def listar():
        """Devuelve todas las asignaturas como lista de objetos Asignatura."""
        con = obtener_conexion()
        filas = con.execute("SELECT * FROM asignaturas ORDER BY nivel, nombre").fetchall()
        con.close()
        return [Asignatura(f["codigo_asignatura"], f["nombre"], f["nivel"], f["horas_requeridas"]) for f in filas]
