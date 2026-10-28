"""Clase Horario: es el centro del diagrama. Relaciona un Docente, una Asignatura,
un Aula y un PeriodoAcademico (guardamos el id/código de cada uno)."""
from base_datos.conexion import obtener_conexion
from clases.aula import Aula

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]


class Horario:
    def __init__(self, id_horario, dia_semana, hora_inicio, hora_fin, estado,
                 docente_id, codigo_asignatura, codigo_aula, codigo_periodo):
        self._id_horario = id_horario
        self._dia_semana = dia_semana
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
        self._estado = estado
        # Relaciones con otras clases
        self._docente_id = docente_id
        self._codigo_asignatura = codigo_asignatura
        self._codigo_aula = codigo_aula
        self._codigo_periodo = codigo_periodo

    def validar_cruce_horarios(self):
        """True si HAY cruce: el docente o el aula ya están ocupados a esa hora."""
        con = obtener_conexion()
        docente_ocupado = con.execute(
            "SELECT COUNT(*) FROM horarios WHERE docente_id = ? AND dia_semana = ? AND estado = 'Activo' "
            "AND hora_inicio < ? AND hora_fin > ? AND id_horario != ?",
            (self._docente_id, self._dia_semana, self._hora_fin, self._hora_inicio, self._id_horario or 0)
        ).fetchone()[0] > 0
        con.close()
        aula_libre = Aula(self._codigo_aula).verificar_disponibilidad(
            self._dia_semana, self._hora_inicio, self._hora_fin, self._id_horario)
        return docente_ocupado or not aula_libre

    def mostrar_detalle(self):
        """Devuelve un diccionario con el horario ya con nombres (no solo códigos)."""
        lista = Horario.listar_detallado("h.id_horario = ?", (self._id_horario,))
        return lista[0] if lista else None

    def guardar(self):
        """INSERT en la base de datos. Devuelve el id nuevo."""
        con = obtener_conexion()
        cur = con.execute(
            "INSERT INTO horarios (dia_semana, hora_inicio, hora_fin, estado, docente_id, "
            "codigo_asignatura, codigo_aula, codigo_periodo) VALUES (?,?,?,?,?,?,?,?)",
            (self._dia_semana, self._hora_inicio, self._hora_fin, self._estado, self._docente_id,
             self._codigo_asignatura, self._codigo_aula, self._codigo_periodo))
        con.commit()
        self._id_horario = cur.lastrowid
        con.close()
        return self._id_horario

    def actualizar(self, dia_semana, hora_inicio, hora_fin, estado):
        """UPDATE de los campos editables."""
        self._dia_semana, self._hora_inicio = dia_semana, hora_inicio
        self._hora_fin, self._estado = hora_fin, estado
        con = obtener_conexion()
        con.execute("UPDATE horarios SET dia_semana=?, hora_inicio=?, hora_fin=?, estado=? WHERE id_horario=?",
                    (dia_semana, hora_inicio, hora_fin, estado, self._id_horario))
        con.commit()
        con.close()

    @staticmethod
    def buscar(id_horario):
        con = obtener_conexion()
        f = con.execute("SELECT * FROM horarios WHERE id_horario = ?", (id_horario,)).fetchone()
        con.close()
        if f is None:
            return None
        return Horario(f["id_horario"], f["dia_semana"], f["hora_inicio"], f["hora_fin"], f["estado"],
                       f["docente_id"], f["codigo_asignatura"], f["codigo_aula"], f["codigo_periodo"])

    @staticmethod
    def listar_detallado(condicion="", parametros=()):
        """Consulta con JOIN que trae nombres de docente, asignatura y aula.
        Sirve para las tablas de las vistas (admin, docente y estudiante)."""
        sql = ("SELECT h.*, a.nombre AS asignatura, a.nivel, u.nombres || ' ' || u.apellidos AS docente, "
               "au.ubicacion AS ubicacion FROM horarios h "
               "JOIN asignaturas a ON a.codigo_asignatura = h.codigo_asignatura "
               "JOIN usuarios u ON u.id = h.docente_id "
               "JOIN aulas au ON au.codigo_aula = h.codigo_aula")
        if condicion:
            sql += " WHERE " + condicion
        con = obtener_conexion()
        filas = [dict(f) for f in con.execute(sql, parametros).fetchall()]
        con.close()
        # Ordenamos por día de la semana y luego por hora
        return sorted(filas, key=lambda f: (DIAS.index(f["dia_semana"]), f["hora_inicio"]))
    
    def guardar_con_validacion(self):
        """Intenta guardar el horario solo si pasa la validación de cruces."""
        if self.validar_cruce_horarios():
            print("[-] Error: No se puede guardar. Existe un cruce de horario para el docente o el aula.")
            return None
        
        # Si no hay cruces, procede a guardar normalmente
        return self.guardar()
