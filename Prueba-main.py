from administrador import Administrador
from docente import Docente
from asignatura import Asignatura
from aula import Aula
from periodo_academico import PeriodoAcademico

if __name__ == "__main__":
    # 1. Crear Periodo Académico
    periodo = PeriodoAcademico("2026-2", "2026-09-01", "2027-01-31")
    periodo.activarPeriodo()

    # 2. Crear Usuarios (Administrador y Docente)
    admin = Administrador("1310000001", "Gipson Javier", "Saltos Palacios", "gsaltos@uleam.edu.ec", "admin123", "Coordinador TI")
    docente = Docente("1309999999", "Jharol Antonio", "Ormaza Sabando", "jormaza@uleam.edu.ec", "docente123", "Ingeniería de Software", 20)

    # 3. Iniciar sesión
    admin.iniciarSesion("gsaltos@uleam.edu.ec", "admin123")

    # 4. Crear Asignatura y Aula
    poo = Asignatura("TI-301", "Programación Orientada a Objetos", "Tercero B", 4)
    lab = Aula("LAB-204", 35, "Laboratorio", "Facultad Ciencias de la Vida y Tecnologías")

    print(poo.obtenerDetalles())

    # 5. Crear y gestionar Horario
    h1 = admin.crearHorario(poo, lab, idHorario="H-101", diaSemana="Miércoles", horaInicio="07:00", horaFin="09:00", docente=docente)
    periodo.agregarHorario(h1)

    # 6. Consultar horario desde el Docente
    docente.consultarHorario()
