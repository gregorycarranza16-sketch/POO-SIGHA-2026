class Paralelo:
    def _init_(self, nombre, nivel, capacidad_maxima):
        self.nombre = nombre
        self.nivel = nivel
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if len(self.estudiantes) < self.capacidad_maxima:
            self.estudiantes.append(estudiante)
            return True
        else:
            return False

    def mostrar_info(self):
        return f"Paralelo {self.nombre} - Nivel {self.nivel} | Inscritos: {len(self.estudiantes)}/{self.capacidad_maxima}"
