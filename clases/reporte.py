class Reporte:
    def _init_(self, id_reporte, fecha_generacion):
        self.id_reporte = id_reporte
        self.fecha_generacion = fecha_generacion

    def generar_ficha_docente(self, docente):
        nombre = docente.obtener_nombre_completo()
        return f"[REPORTE {self.fecha_generacion}] Docente: {nombre} | Carga: {docente.horas_asignadas}/{docente.max_horas}h"
