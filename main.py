"""Punto de entrada: crea la base de datos (si hace falta) y arranca el sitio web.
Ejecutar con:  python main.py   y abrir http://127.0.0.1:5000"""
from base_datos.conexion import crear_tablas, cargar_datos_ejemplo
from interfaz.app import app

if __name__ == "__main__":
    crear_tablas()
    cargar_datos_ejemplo()
    app.run(debug=True)
