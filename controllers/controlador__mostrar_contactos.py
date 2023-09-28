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

    def llamar_contacto_especifico_con_id(self, id):
        """
        Descripcion:
            Dado un id existente realiza una consulta para traer el registro

        Args:
            id (int) : Id del registro necesitado

        Reutrns:
            list[tuple] : Lista con los datos del registro [(id, nombre, numero, pais, fecha_na)]
        """
        import sqlite3

        # Conexion sqlite3, consulta y cierre conexion
        conn = sqlite3.connect('./data/contactos.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contactos where ID = ?", (id,))
        resultados = cursor.fetchall()
        conn.close()
        return resultados
