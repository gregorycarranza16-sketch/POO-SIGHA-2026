def limpiar_texto(texto):
    """Limpia espacios y formatea texto para las vistas del SIGHA."""
    if not texto:
        return ""
    return texto.strip().title()

def validar_cedula_ecuador(cedula):
    """Validación rápida para cédulas de estudiantes o docentes."""
    return len(cedula) == 10 and cedula.isdigit()
