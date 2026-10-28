class Asignatura:
    def __init__(self, codigo, nombre, nivel, horas_requeridas):
        self.codigo = codigo
        self.nombre = nombre
        self.nivel = nivel
        self.horas_requeridas = horas_requeridas

    def mostrar_info(self):
        return f"Asignatura: {self.codigo} - {self.nombre} | Horas: {self.horas_requeridas}h"
