import customtkinter


class ControladorAgregarContacto:
    def __init__(self, master) -> None:
        self.master = master

    def insertar_datos(self):

        # Recogiendo datos necesarios
        nombre = self.master.vista_agregar_contacto.entrada['nombre'].get()
        numero = self.master.vista_agregar_contacto.entrada['numero'].get()
        pais = self.master.vista_agregar_contacto.entrada['pais'].get()
        fecha_na = self.master.vista_agregar_contacto.entrada['fecha_na'].get()

        # Verificando datos
        mi_booleano = self.vericacion_datos(
            nombre, numero, pais, fecha_na)

        # Si son datos validos los guardamos
        if mi_booleano:
            self.verificiado(nombre, numero, pais, fecha_na)
        else:
            return 0

    def verificiado(self, nombre, numero, pais, fecha_na):
        # Conectando con sqlite3
        import sqlite3
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

    def vericacion_datos(self, nombre, numero, pais, fecha_na):
        # Verifia datos, muestra mensaje de resultado.
        import re
        telefono_regex = r'^\+\d{1,3}[-\s]+\d{1,14}[-\s]+\d{1,14}$'
        
        # Creo label para mostrar resultado
        self.label_error = customtkinter.CTkLabel(self.master.vista_agregar_contacto)

        # Verificar telefono
        if re.match(telefono_regex, numero):
            print('Numero valido')
            self.label_error.configure(bg_color='green')
            self.label_error.configure(text="Numer valido")
            self.label_error.grid(column=0, row=6)
            return True

        else:
            print('Numero invalido')
            self.label_error.configure(bg_color='red')
            self.label_error.configure(text="Numero invalido")
            self.label_error.grid(column=0, row=6)
            return False


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
        self.master.vista_contacto.controlador.mostrar_datos(
            nombre, numero, pais, fecha_na)
