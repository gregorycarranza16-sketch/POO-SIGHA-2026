class Aula:
    def __init__(self, codigo, capacidad, tipo):
        self.codigo = codigo
        self.capacidad = capacidad
        self.tipo = tipo

    def validar_aforo(self, cantidad_alumnos):
        if cantidad_alumnos <= self.capacidad:
            return True
        else:
            return False

    def mostrar_info(self):
        return f"Aula: {self.codigo} | Tipo: {self.tipo} | Capacidad: {self.capacidad} alumnos"
