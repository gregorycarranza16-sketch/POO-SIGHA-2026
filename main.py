from clases.sistema import SistemaSIGHA  # O la clase controladora principal que definimos

def main():
    print("==================================================")
    print("      SISTEMA DE GESTIÓN DE HORARIOS (SIGHA)     ")
    print("==================================================")
    
    try:
        # Inicializamos el sistema aplicando los principios de POO
        app_sigla = SistemaSIGHA()
        app_sigla.ejecutar()
    except Exception as e:
        print(f"[-] Ocurrió un error al iniciar el sistema: {e}")

if __name__ == "__main__":
    main()
