class ControladorAgregarContacto:
    def __init__(self, master) -> None:
        self.master = master

    def insertar_datos(self):
        import sqlite3

        # Recogiendo datos necesarios
        nombre = self.master.vista_agregar_contacto.entrada['nombre'].cget()
        numero = self.master.vista_agregar_contacto.entrada['numero'].cget()
        pais = self.master.vista_agregar_contacto.entrada['pais'].cget()
        fecha_na = self.master.vista_agregar_contacto.entrada['fecha_na'].cget()

        # Conectando con sqlite3
        conn = sqlite3.connect('./data/contactos.db')
        cursor = conn.cursor()

        # Ejecutando consulta de inserccion
        cursor.execute(
            '''INSERT INTO contactos (Nombre, Nuemero, Pais, FechaNacimieno) VALUES (?, ?, ?, ?)''',
            (nombre, numero, pais, fecha_na))
        conn.commit()
        
        # Limpiando datos
        self.limpiar_datos()

    def limpiar_datos(self):
        # nombre = self.master.vista_agregar_contacto.entrada['nombre'].cget()
        # numero = self.master.vista_agregar_contacto.entrada['numero'].cget()
        # pais = self.master.vista_agregar_contacto.entrada['pais'].cget()
        # fecha_na = self.master.vista_agregar_contacto.entrada['fecha_na'].cget()
        return 0