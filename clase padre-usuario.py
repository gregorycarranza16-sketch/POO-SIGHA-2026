class Usuario:
    def __init__(self, identificacion: str, nombres: str, apellidos: str, correo: str, clave: str):
        # Atributos protegidos (#)
        self._identificacion = identificacion
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        # Atributo privado (-)
        self.__clave = clave
        self._sesion_activa = False

    def iniciarSesion(self, correo: str, clave: str) -> bool:
        if self._correo == correo and self.__clave == clave:
            self._sesion_activa = True
            print(f"[OK] Bienvenido/a {self._nombres} {self._apellidos}.")
            return True
        print("[ERROR] Credenciales incorrectas.")
        return False

    def cerrarSesion(self) -> None:
        self._sesion_activa = False
        print(f"[INFO] Sesión cerrada para {self._correo}.")

    @property
    def nombre_completo(self) -> str:
        return f"{self._nombres} {self._apellidos}"
