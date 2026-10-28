"""Clase PeriodoAcademico. Contiene (composición) a muchos Horarios."""
from base_datos.conexion import obtener_conexion


class PeriodoAcademico:
    def __init__(self, codigo_periodo, fecha_inicio, fecha_fin, estado):
        self._codigo_periodo = codigo_periodo
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._estado = estado

    @property
    def datos(self):
        return {"codigo": self._codigo_periodo, "inicio": self._fecha_inicio,
                "fin": self._fecha_fin, "estado": self._estado}

    def _cambiar_estado(self, nuevo_estado):
        con = obtener_conexion()
        con.execute("UPDATE periodos SET estado = ? WHERE codigo_periodo = ?", (nuevo_estado, self._codigo_periodo))
        con.commit()
        con.close()
        self._estado = nuevo_estado

    def activar_periodo(self):
        self._cambiar_estado("Activo")

    def finalizar_periodo(self):
        self._cambiar_estado("Finalizado")

    @staticmethod
    def buscar(codigo):
        con = obtener_conexion()
        f = con.execute("SELECT * FROM periodos WHERE codigo_periodo = ?", (codigo,)).fetchone()
        con.close()
        return PeriodoAcademico(f["codigo_periodo"], f["fecha_inicio"], f["fecha_fin"], f["estado"]) if f else None

    @staticmethod
    def listar():
        con = obtener_conexion()
        filas = con.execute("SELECT * FROM periodos ORDER BY fecha_inicio DESC").fetchall()
        con.close()
        return [PeriodoAcademico(f["codigo_periodo"], f["fecha_inicio"], f["fecha_fin"], f["estado"]) for f in filas]
