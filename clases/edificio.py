class Edificio:
    def _init_(self, codigo, nombre, ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.aulas = []

    def agregar_aula(self, aula):
        self.aulas.append(aula)

    def mostrar_info(self):
        return f"Edificio {self.codigo} - {self.nombre} ({self.ubicacion}) | Total Aulas: {len(self.aulas)}"
