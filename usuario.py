class Usuario:
    def __init__(self, identificacion, nombres, apellidos, correo, clave):
        self._identificacion = identificacion
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        self.__clave = clave

    def iniciarSesion(self, correo, clave):
        pass

    def cerrarSesion(self):
        pass
