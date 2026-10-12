from usuario import Usuario  # Importamos la clase padre

class Docente(Usuario):
    def __init__(self, identificacion, nombres, apellidos, correo, clave, especialidad, maxHorasSemanales):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self.__especialidad = especialidad
        self.__maxHorasSemanales = maxHorasSemanales

    def consultarHorario(self):
        pass
