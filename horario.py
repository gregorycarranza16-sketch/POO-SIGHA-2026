class Horario:
    def __init__(self, id_horario, dia, hora_inicio, hora_fin):
        self.id_horario = id_horario
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def comprobar_cruce(self, otro_dia, otra_hora_inicio):
        if self.dia == otro_dia and self.hora_inicio == otra_hora_inicio:
            return True
        else:
            return False

    def mostrar_info(self):
        return f"Horario {self.id_horario}: {self.dia} de {self.hora_inicio}:00 a {self.hora_fin}:00"
