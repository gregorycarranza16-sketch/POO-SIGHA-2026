# Definición de la Clase Docente
class Docente:
    def __init__(self, cedula, nombres, titulo, horas_maximas):
        self.cedula = cedula           # Atributo: Cédula del profesor
        self.nombres = nombres         # Atributo: Nombres completos
        self.titulo = titulo           # Atributo: Título académico
        self.horas_maximas = horas_maximas # Atributo: Límite de horas semanales
        self.horas_asignadas = 0       # Atributo extra para llevar la cuenta

    # Método para mostrar los datos
    def mostrar_info(self):
        print(f"Docente: {self.titulo} {self.nombres} | Horas Max: {self.horas_maximas}")


# Definición de la Clase Aula
class Aula:
    def __init__(self, codigo, tipo, capacidad, ubicacion):
        self.codigo = codigo           # Atributo: Código del aula (Ej. A-101)
        self.tipo = tipo               # Atributo: Laboratorio o Teórica
        self.capacidad = capacidad     # Atributo: Cantidad de estudiantes
        self.ubicacion = ubicacion     # Atributo: Bloque o piso

    # Método para mostrar los datos
    def mostrar_info(self):
        print(f"Aula: {self.codigo} ({self.tipo}) | Capacidad: {self.capacidad} alumnos")


# --- PRUEBA DEL CÓDIGO (Instanciación de Objetos) ---
# Aquí creamos un profesor y un aula reales para la demostración:

profesor1 = Docente("1312345678", "Juan Pérez", "Ingeniero", 20)
aula1 = Aula("LAB-01", "Laboratorio de Cómputo", 30, "Bloque B")

print("--- SISTEMA SIGHA: DEMOSTRACIÓN DE AVANCE ---")
profesor1.mostrar_info()
aula1.mostrar_info()
