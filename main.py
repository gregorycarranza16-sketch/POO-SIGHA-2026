from docente import Docente
from aula import Aula

def main():
    print("=== AVANCE DEL PROYECTO SIGHA ===")
    print("Creando objetos en memoria...\n")

    profe1 = Docente("1312345678", "Jharol", "Ormaza", "jharol@uleam.edu.ec", "1234", "Software", 40)
    aula_lab = Aula("LAB-01", 30, "Laboratorio")

    print(profe1.mostrar_info())
    print(aula_lab.mostrar_info())
    print("-" * 40)

    estudiantes = 35
    print(f"Intentando meter {estudiantes} estudiantes en {aula_lab.codigo}...")
    
    if aula_lab.validar_aforo(estudiantes) == True:
        print("Aforo correcto, si caben.")
    else:
        print("Error: Hay demasiados estudiantes para esta aula.")

    print("-" * 40)

    horas_materia = 6
    print(f"Intentando asignar {horas_materia} horas al docente...")
    
    if profe1.asignar_horas(horas_materia) == True:
        print("Horas asignadas correctamente.")
    else:
        print("Error: El docente supera su limite de horas.")

    print(profe1.mostrar_info())

if __name__ == "__main__":
    main()
