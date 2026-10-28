class GeneradorReportes:
    @staticmethod
    def exportar_resumen_horarios(horarios):
        """Genera un reporte en texto plano formateado con los horarios activos."""
        reporte = "==================================================\n"
        reporte += "       REPORTE OFICIAL DE HORARIOS - SIGHA      \n"
        reporte += "==================================================\n"
        for h in horarios:
            reporte += f"Día: {h.get('dia_semana')} | Hora: {h.get('hora_inicio')} - {h.get('hora_fin')}\n"
            reporte += f"Asignatura: {h.get('asignatura')} | Docente: {h.get('docente')}\n"
            reporte += "--------------------------------------------------\n"
        return reporte
