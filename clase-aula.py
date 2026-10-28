class Aula:
    def __init__(self, codigoAula: str, capacidad: int, tipo: str, ubicacion: str):
        # Atributos privados (-)
        self.__codigoAula = codigoAula
        self.__capacidad = capacidad
        self.__tipo = tipo
        self.__ubicacion = ubicacion
        self.__horarios_asignados = []  # Para validar disponibilidad (0..*)

    def verificarDisponibilidad(self, dia: str, horaInicio: str, horaFin: str) -> bool:
        for h in self.__horarios_asignados:
            if h.diaSemana == dia and h.estado == "Activo":
                # Verifica si hay solapamiento de horas
                if not (horaFin <= h.horaInicio or horaInicio >= h.horaFin):
                    return False
        return True

    def agregarHorario(self, horario) -> None:
        self.__horarios_asignados.append(horario)

    @property
    def codigoAula(self) -> str:
        return self.__codigoAula
