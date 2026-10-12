from usuario import Usuario  # Importamos la clase padre

class Administrador(Usuario):
    def __init__(self, identificacion, nombres, apellidos, correo, clave, cargo):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self.__cargo = cargo

    def crearHorario(self, asignatura, aula):
        pass

    def modificarHorario(self, idHorario):
        pass
