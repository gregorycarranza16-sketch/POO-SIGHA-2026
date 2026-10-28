class Usuario:
    def __init__(self, identificacion, nombres, apellidos, correo, clave):
        self._identificacion = identificacion
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        self._clave = clave

    def obtener_nombre_completo(self):
        return f"{self._nombres} {self._apellidos}"
