from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, identificacion, nombres, apellidos, correo, clave, cargo):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self.cargo = cargo

    def mostrar_info(self):
        nombre = self.obtener_nombre_completo()
        return f"Administrador: {nombre} | Cargo: {self.cargo}"
