class Horario:
    def __init__(self, idHorario: str, diaSemana: str, horaInicio: str, horaFin: str, 
                 estado: str, asignatura=None, aula=None, docente=None):
        # Atributos privados (-)
        self.__idHorario = idHorario
        self.__diaSemana = diaSemana
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin
        self.__estado = estado
        
        # Relaciones (1 Asignatura, 1 Aula, 1 Docente)
        self.__asignatura = asignatura
        self.__aula = aula
        self.__docente = docente

    def validarCruceHorarios(self, otro_horario) -> bool:
        """Retorna True si hay cruce de horario con otro objeto Horario en el mismo día."""
        if self.__diaSemana == otro_horario.diaSemana:
            if not (self.__horaFin <= otro_horario.horaInicio or self.__horaInicio >= otro_horario.horaFin):
                return True  # Hay cruce
        return False

    def mostrarDetalle(self) -> str:
        asig = self.__asignatura.nombre if self.__asignatura else "Sin asignar"
        aula = self.__aula.codigoAula if self.__aula else "Sin aula"
        doc = self.__docente.nombre_completo if self.__docente else "Sin docente"
        return (f"Horario [{self.__idHorario}] - {self.__diaSemana} ({self.__horaInicio} - {self.__horaFin}) | "
                f"Materia: {asig} | Aula: {aula} | Docente: {doc} | Estado: {self.__estado}")

    # Getters y Setters necesarios para las demás clases
    @property
    def idHorario(self) -> str:
        return self.__idHorario

    @property
    def diaSemana(self) -> str:
        return self.__diaSemana

    @property
    def horaInicio(self) -> str:
        return self.__horaInicio

    @property
    def horaFin(self) -> str:
        return self.__horaFin

    @property
    def estado(self) -> str:
        return self.__estado

    def actualizarDatos(self, diaSemana: str, horaInicio: str, horaFin: str, estado: str) -> None:
        self.__diaSemana = diaSemana
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin
        self.__estado = estado
