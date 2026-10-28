import shutil
import os

def crear_respaldo_sqlite():
    """Crea una copia de seguridad local de la base de datos del SIGHA."""
    db_origen = "sigla.db"
    db_destino = "sigla_backup.db"
    if os.path.exists(db_origen):
        shutil.copy(db_origen, db_destino)
        print("[+] Respaldo de base de datos generado con éxito.")
    else:
        print("[-] No se encontró la base de datos principal para respaldar.")

if __name__ == "__main__":
    crear_respaldo_sqlite()
