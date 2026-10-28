from clases.docente import Docente
from clases.administrador import Administrador
from clases.estudiante import Estudiante
from clases.aula import Aula
from clases.asignatura import Asignatura
from clases.horario import Horario
from clases.periodo_academico import PeriodoAcademico

def main():
    print("=== SISTEMA SIGHA - EJECUCIÓN PRINCIPAL ===")

    # Instanciación de usuarios
    profe = Docente("1312345678", "Jharol", "Ormaza", "jharol@uleam.edu.ec", "1234", "Software", 40)
    admin = Administrador("1309876543", "Carlos", "Mendoza", "carlos@uleam.edu.ec", "admin123", "Coordinador")
    alumno = Estudiante("1311223344", "Gregory", "Carranza", "gregory@uleam.edu.ec", "5678", "Software", 3)

    usuarios = [profe, admin, alumno]

    print("\n--- Demostración de Polimorfismo ---")
    for usuario in usuarios:
        print(usuario.mostrar_info())

    print("\n--- Prueba de Infraestructura ---")
    aula1 = Aula("LAB-01", 30, "Laboratorio")
    print(aula1.mostrar_info())

    if aula1.validar_aforo(25):
        print("Aforo permitido.")
    else:
        print("Excede la capacidad del aula.")

if __name__ == "__main__":
    main()
