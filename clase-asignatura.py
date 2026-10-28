class Asignatura:
    def __init__(self, codigoAsignatura: str, nombre: str, nivel: str, horasRequeridas: int):
        # Atributos privados (-)
        self.__codigoAsignatura = codigoAsignatura
        self.__nombre = nombre
        self.__nivel = nivel
        self.__horasRequeridas = horasRequeridas

    def obtenerDetalles(self) -> str:
        return (f"Código: {self.__codigoAsignatura} | Asignatura: {self.__nombre} | "
                f"Nivel: {self.__nivel} | Horas Req.: {self.__horasRequeridas}")

    @property
    def nombre(self) -> str:
        return self.__nombre
