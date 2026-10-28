from usuario import Usuario

class Docente(Usuario):
    def __init__(self, identificacion, nombres, apellidos, correo, clave, especialidad, max_horas):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self.especialidad = especialidad
        self.max_horas = max_horas
        self.horas_asignadas = 0

    def asignar_horas(self, horas_nuevas):
        if (self.horas_asignadas + horas_nuevas) <= self.max_horas:
            self.horas_asignadas = self.horas_asignadas + horas_nuevas
            return True
        else:
            return False

    def mostrar_info(self):
        nombre = self.obtener_nombre_completo()
        return f"Docente: {nombre} | Especialidad: {self.especialidad} | Horas: {self.horas_asignadas}/{self.max_horas}"from usuario import Usuario

class Docente(Usuario):
    def __init__(self, identificacion, nombres, apellidos, correo, clave, especialidad, max_horas):
        super().__init__(identificacion, nombres, apellidos, correo, clave)
        self.especialidad = especialidad
        self.max_horas = max_horas
        self.horas_asignadas = 0

    def asignar_horas(self, horas_nuevas):
        if (self.horas_asignadas + horas_nuevas) <= self.max_horas:
            self.horas_asignadas = self.horas_asignadas + horas_nuevas
            return True
        else:
            return False

    def mostrar_info(self):
        nombre = self.obtener_nombre_completo()
        return f"Docente: {nombre} | Especialidad: {self.especialidad} | Horas: {self.horas_asignadas}/{self.max_horas}"
