import customtkinter


class ControladorAgregarContacto:
    def __init__(self, master) -> None:
        self.master = master

    def insertar_datos(self):
        import sqlite3

        # Recogiendo datos necesarios
        nombre = self.master.vista_agregar_contacto.entrada['nombre'].get()
        numero = self.master.vista_agregar_contacto.entrada['numero'].get()
        pais = self.master.vista_agregar_contacto.entrada['pais'].get()
        fecha_na = self.master.vista_agregar_contacto.entrada['fecha_na'].get()

        # Conectando con sqlite3
        conn = sqlite3.connect('./data/contactos.db')
        cursor = conn.cursor()

        # Ejecutando consulta de inserccion, guardar ultimo id
        cursor.execute(
            '''INSERT INTO contactos (Nombre, Numero, Pais, FechaNacimiento) VALUES (?, ?, ?, ?)''',
            (nombre, numero, pais, fecha_na))
        conn.commit()
        self.nuevo_id = cursor.lastrowid

        # Limpiando datos de entradas   
        self.limpiar_campos()

        # Cambiar para ver el contacto agregado
        self.mostrar_contacto(nombre, numero, pais, fecha_na)

    def limpiar_campos(self):
        """
        Deja vacia las entradas
        """
        for entrada in self.master.vista_agregar_contacto.entrada.values():
            entrada.delete(0, customtkinter.END)

    def cancelar(self):
        """
        Regresa al menu principal al cancelara la operacion
        """
        self.master.cambiar_frame(self.master.vista_inicio)

    def mostrar_contacto(self, nombre, numero, pais, fecha_na):
        """
        Sirve para ver el contacto agregado
        """
        self.master.cambiar_frame(self.master.vista_contacto)
        self.master.vista_contacto.controlador.mostrar_datos(nombre, numero, pais, fecha_na)
