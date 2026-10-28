"""Conexión y configuración de la base de datos (SQLite).
SQLite guarda todo en un solo archivo (horarios.db), por eso no hay que instalar nada."""
import os
import sqlite3
from werkzeug.security import generate_password_hash  # viene incluido con Flask

# El archivo de la base de datos queda dentro de esta misma carpeta
RUTA_BD = os.path.join(os.path.dirname(__file__), "horarios.db")


def obtener_conexion():
    """Abre una conexión. row_factory permite leer columnas por nombre: fila["correo"]."""
    con = sqlite3.connect(RUTA_BD)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")  # activa las llaves foráneas
    return con


def crear_tablas():
    """Crea una tabla por cada clase del diagrama (si no existen todavía)."""
    con = obtener_conexion()
    con.executescript("""
    -- Usuario, Docente, Estudiante y Administrador comparten una sola tabla.
    -- La columna 'rol' indica de qué clase es cada fila; las demás columnas
    -- específicas (especialidad, cargo, nivel...) quedan vacías si no aplican.
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombres TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        correo TEXT NOT NULL UNIQUE,
        clave TEXT NOT NULL,                 -- se guarda cifrada (hash), nunca en texto plano
        rol TEXT NOT NULL CHECK (rol IN ('docente','estudiante','administrador')),
        especialidad TEXT,                   -- solo Docente
        max_horas_semanales INTEGER,         -- solo Docente
        cargo TEXT,                          -- solo Administrador
        nivel INTEGER                        -- solo Estudiante
    );
    CREATE TABLE IF NOT EXISTS asignaturas (
        codigo_asignatura TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel INTEGER NOT NULL,
        horas_requeridas INTEGER NOT NULL
    );
    CREATE TABLE IF NOT EXISTS aulas (
        codigo_aula TEXT PRIMARY KEY,
        capacidad INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        ubicacion TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS periodos (
        codigo_periodo TEXT PRIMARY KEY,
        fecha_inicio TEXT NOT NULL,
        fecha_fin TEXT NOT NULL,
        estado TEXT NOT NULL DEFAULT 'Inactivo'
    );
    -- Relación "Docente imparte Asignatura" (muchos a muchos)
    CREATE TABLE IF NOT EXISTS docente_asignatura (
        docente_id INTEGER REFERENCES usuarios(id),
        codigo_asignatura TEXT REFERENCES asignaturas(codigo_asignatura),
        PRIMARY KEY (docente_id, codigo_asignatura)
    );
    -- Horario: une a un docente, una asignatura, un aula y un período
    CREATE TABLE IF NOT EXISTS horarios (
        id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
        dia_semana TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,           -- formato "HH:MM"
        hora_fin TEXT NOT NULL,
        estado TEXT NOT NULL DEFAULT 'Activo',
        docente_id INTEGER NOT NULL REFERENCES usuarios(id),
        codigo_asignatura TEXT NOT NULL REFERENCES asignaturas(codigo_asignatura),
        codigo_aula TEXT NOT NULL REFERENCES aulas(codigo_aula),
        codigo_periodo TEXT NOT NULL REFERENCES periodos(codigo_periodo)
    );
    """)
    con.commit()
    con.close()


def cargar_datos_ejemplo():
    """Inserta datos de prueba solo la primera vez (si no hay usuarios)."""
    con = obtener_conexion()
    if con.execute("SELECT COUNT(*) FROM usuarios").fetchone()[0] > 0:
        con.close()
        return
    h = generate_password_hash  # cifra las contraseñas
    # (nombres, apellidos, correo, clave, rol, especialidad, max_horas, cargo, nivel)
    # Los ids se asignan en este orden: 1 = admin, 2 = Carlos, 3 = Lucía, 4 = María...
    con.executemany(
        "INSERT INTO usuarios (nombres, apellidos, correo, clave, rol, especialidad, max_horas_semanales, cargo, nivel) "
        "VALUES (?,?,?,?,?,?,?,?,?)", [
            ("Ana", "Pérez", "admin@uni.edu", h("admin123"), "administrador", None, None, "Coordinadora académica", None),
            ("Carlos", "Mora", "docente@uni.edu", h("docente123"), "docente", "Programación", 20, None, None),
            ("Lucía", "Vera", "estudiante@uni.edu", h("estudiante123"), "estudiante", None, None, None, 1),
            ("María", "Salazar", "maria@uni.edu", h("docente123"), "docente", "Bases de Datos", 18, None, None),
            ("Jorge", "Intriago", "jorge@uni.edu", h("docente123"), "docente", "Redes", 16, None, None),
            ("Patricia", "Zambrano", "patricia@uni.edu", h("docente123"), "docente", "Matemáticas", 20, None, None),
            ("Diego", "Cedeño", "diego@uni.edu", h("estudiante123"), "estudiante", None, None, None, 2),
            ("Valeria", "Mendoza", "valeria@uni.edu", h("estudiante123"), "estudiante", None, None, None, 1),
        ])
    con.executemany("INSERT INTO asignaturas VALUES (?,?,?,?)", [
        ("PRG101", "Programación I", 1, 4), ("MAT101", "Matemática Discreta", 1, 4),
        ("BDD201", "Bases de Datos", 2, 4), ("RED201", "Redes de Computadoras", 2, 3),
        ("ING301", "Ingeniería de Software", 3, 4)])
    con.executemany("INSERT INTO aulas VALUES (?,?,?,?)", [
        ("A-101", 30, "Laboratorio", "Bloque A, piso 1"), ("A-102", 30, "Laboratorio", "Bloque A, piso 1"),
        ("B-201", 40, "Aula teórica", "Bloque B, piso 2"), ("B-202", 40, "Aula teórica", "Bloque B, piso 2"),
        ("C-301", 80, "Auditorio", "Bloque C, piso 3")])
    con.execute("INSERT INTO periodos VALUES ('2026-2','2026-09-01','2027-01-31','Activo')")
    con.execute("INSERT INTO periodos VALUES ('2027-1','2027-03-01','2027-07-31','Inactivo')")
    # Docente imparte Asignatura: (id del docente, código de la asignatura)
    con.executemany("INSERT INTO docente_asignatura VALUES (?,?)", [
        (2, "PRG101"), (2, "ING301"), (4, "BDD201"), (4, "ING301"), (5, "RED201"), (6, "MAT101")])
    # Horarios de ejemplo: (día, inicio, fin, docente, asignatura, aula)
    for dia, ini, fin, doc, asig, aula in [
            ("Lunes", "08:00", "10:00", 2, "PRG101", "A-101"),
            ("Martes", "10:00", "12:00", 4, "BDD201", "B-202"),
            ("Miércoles", "08:00", "10:00", 6, "MAT101", "B-201"),
            ("Jueves", "14:00", "16:00", 5, "RED201", "A-102")]:
        con.execute("INSERT INTO horarios (dia_semana,hora_inicio,hora_fin,estado,docente_id,"
                    "codigo_asignatura,codigo_aula,codigo_periodo) VALUES (?,?,?,'Activo',?,?,?,'2026-2')",
                    (dia, ini, fin, doc, asig, aula))
    con.commit()
    con.close()
