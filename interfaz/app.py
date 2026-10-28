"""Sitio web con Flask: login y una vista distinta según el rol del usuario."""
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from clases import (buscar_usuario_por_correo, buscar_usuario_por_id, Horario, Asignatura,
                    Aula, PeriodoAcademico, Docente, DIAS)

app = Flask(__name__)
app.secret_key = "clave-secreta-solo-para-la-tarea"  # Flask la usa para firmar la sesión


def usuario_actual():
    """Devuelve el objeto Usuario de la sesión (o None si no ha iniciado sesión)."""
    id_usuario = session.get("usuario_id")
    return buscar_usuario_por_id(id_usuario) if id_usuario else None


def rol_requerido(rol):
    """Decorador: solo deja entrar a la ruta si el usuario tiene ese rol."""
    def decorador(vista):
        @wraps(vista)
        def envoltura(*args, **kwargs):
            usuario = usuario_actual()
            if usuario is None:
                return redirect(url_for("login"))
            if usuario.rol != rol:
                flash("No tienes permiso para ver esa página.")
                return redirect(url_for("inicio"))
            return vista(usuario, *args, **kwargs)
        return envoltura
    return decorador


@app.route("/")
def inicio():
    """Manda a cada usuario a su panel (el nombre del rol coincide con el de la ruta)."""
    usuario = usuario_actual()
    return redirect(url_for(usuario.rol)) if usuario else redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"].strip()
        clave = request.form["clave"]
        usuario = buscar_usuario_por_correo(correo)
        # iniciar_sesion() es el método de la clase Usuario del diagrama
        if usuario and usuario.iniciar_sesion(correo, clave):
            session["usuario_id"] = usuario.identificacion
            return redirect(url_for("inicio"))
        flash("Correo o clave incorrectos.")
    return render_template("login.html")


@app.route("/logout")
def logout():
    usuario = usuario_actual()
    if usuario:
        usuario.cerrar_sesion()
    session.clear()
    return redirect(url_for("login"))


@app.route("/docente")
@rol_requerido("docente")
def docente(usuario):
    return render_template("docente.html", usuario=usuario, horarios=usuario.consultar_horario())


@app.route("/estudiante")
@rol_requerido("estudiante")
def estudiante(usuario):
    return render_template("estudiante.html", usuario=usuario, horarios=usuario.consultar_horario())


@app.route("/administrador")
@rol_requerido("administrador")
def administrador(usuario):
    return render_template("administrador.html", usuario=usuario,
                           horarios=Horario.listar_detallado(), asignaturas=Asignatura.listar(),
                           aulas=Aula.listar(), periodos=PeriodoAcademico.listar(),
                           docentes=Docente.listar(), dias=DIAS)


@app.route("/administrador/crear", methods=["POST"])
@rol_requerido("administrador")
def crear_horario(usuario):
    f = request.form
    ok, mensaje = usuario.crear_horario(f["asignatura"], f["aula"], int(f["docente"]),
                                        f["periodo"], f["dia"], f["hora_inicio"], f["hora_fin"])
    flash(mensaje)
    return redirect(url_for("administrador"))


@app.route("/administrador/editar/<int:id_horario>", methods=["GET", "POST"])
@rol_requerido("administrador")
def editar_horario(usuario, id_horario):
    if request.method == "POST":
        f = request.form
        ok, mensaje = usuario.modificar_horario(id_horario, f["dia"], f["hora_inicio"], f["hora_fin"], f["estado"])
        flash(mensaje)
        return redirect(url_for("administrador"))
    detalle = Horario.buscar(id_horario).mostrar_detalle()
    return render_template("editar_horario.html", usuario=usuario, h=detalle, dias=DIAS)


@app.route("/administrador/periodo/<codigo>/<accion>", methods=["POST"])
@rol_requerido("administrador")
def cambiar_periodo(usuario, codigo, accion):
    periodo = PeriodoAcademico.buscar(codigo)
    if periodo and accion == "activar":
        periodo.activar_periodo()
    elif periodo and accion == "finalizar":
        periodo.finalizar_periodo()
    return redirect(url_for("administrador"))
