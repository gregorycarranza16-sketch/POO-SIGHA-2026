"""Clase base Usuario. Docente, Estudiante y Administrador heredan de ella.
Convención: un guion bajo (_atributo) indica atributo protegido (# en el diagrama);
_clave es el atributo privado (-). Python no los bloquea, es una convención."""
from werkzeug.security import check_password_hash


class Usuario:
    rol = "usuario"  # cada subclase lo sobrescribe: "docente", "estudiante", "administrador"

    def __init__(self, identificacion, nombres, apellidos, correo, clave):
        self._identificacion = identificacion
        self._nombres = nombres
        self._apellidos = apellidos
        self._correo = correo
        self._clave = clave  # aquí llega la clave ya cifrada (hash)

    @property
    def nombre_completo(self):
        return f"{self._nombres} {self._apellidos}"

    @property
    def identificacion(self):
        return self._identificacion

    def iniciar_sesion(self, correo, clave):
        """Devuelve True si el correo y la clave escritos coinciden con los de este usuario."""
        return correo == self._correo and check_password_hash(self._clave, clave)

    def cerrar_sesion(self):
        """La sesión web se limpia en la capa de interfaz; aquí solo devolvemos un mensaje."""
        return f"Sesión de {self.nombre_completo} cerrada."
