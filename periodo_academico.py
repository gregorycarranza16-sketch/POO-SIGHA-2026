class PeriodoAcademico:
    def __init__(self, codigo, fecha_inicio, fecha_fin):
        self.codigo = codigo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.__estado = "Activo"

    def obtener_estado(self):
        return self.__estado

    def cerrar_periodo(self):
        self.__estado = "Inactivo"
        return "El periodo ha sido cerrado y ya no se pueden hacer horarios."

    def mostrar_info(self):
        return f"Periodo: {self.codigo} | Estado: {self.__estado}"
