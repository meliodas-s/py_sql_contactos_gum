class ControladorMostrarContactos:
    def __init__(self, master) -> None:
        self.master = master

    def llamar_datos(self):
        import sqlite3

        # Conexion sqlite3, consulta y cierre conexion
        conn = sqlite3.connect('./data/contactos.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contactos")
        resultados = cursor.fetchall()
        conn.close()

        # Devolver datos
        return resultados