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
            self.master.vista_mostrar_Contactos.nuevo_contacto(self.nuevo_id)
        else:
            return 0

    def verificiado(self, nombre, numero, pais, fecha_na):
        """
        Descripcion:
            Conecta con la base de datos y guarda el nuevo registro.

        Args:
            self (ControladorAgregarContacto): Objeto
            nombre (str) : Nuevo nombre
            numero (str) : Nuevo numero en el formato correcto
            pais (str) : Pais del sujeto, es valida cualquier entrada de texto. Es opcional, puede estar vacio
            fecha_na (str) : Fechas en formato dd-mm-aaaa

        Returns:
            int : Id del nuevo registro de contacto
        """

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

        # Retornar nuevo id de nuevo contacto, aunque ya es un atributo
        return self.nuevo_id

    def limpiar_campos(self):
        """
        Deja vacia las entradas
        """
        for entrada in self.master.vista_agregar_contacto.entrada.values():
            entrada.delete(0, customtkinter.END)

    def vericacion_datos(self, nombre, numero, pais, fecha_na):
        """
        Verifica que todas las etradas sean validas.

        Args:
            nombre (str): Nombre del contacto
            numero (str): Numero del contacto
            pais (str): Pais del contacto
            fecha_na (str): Fecha de nacimiento del contacto (opcional)

        Returns:
            bool: True si los contactos son validos
        """

        # Verifia datos, muestra mensaje de resultado.
        import re

        # Verificar telefono
        regex = r'^\+\d{1,3}[-\s]+\d{1,14}[-\s]+\d{1,14}$'
        if re.match(regex, numero):
            print('Numero valido')

        else:
            print('Numero invalido')
            self.master.vista_agregar_contacto.label_error.configure(
                text="Numero invalido")
            self.master.vista_agregar_contacto.label_error.grid(
                column=0, row=6, pady=(40, 0), padx=40)
            return False

        # Verifica nombre
        regex = r'.+'
        if re.match(regex, nombre):
            print('Nombre valido')

            # Remuevo el mensaje de error si este existe
            self.master.vista_agregar_contacto.label_error.grid_remove()

        else:
            print('Nombre invalido')
            self.master.vista_agregar_contacto.label_error.configure(
                text="Nombre esta vacio")
            self.master.vista_agregar_contacto.label_error.grid(
                column=0, row=6, pady=(40, 0), padx=40)
            return False

        # Verificar fecha
        regex = r'^\d{2}[-]+\d{2}[-]+\d{4}$'
        if re.match(regex, fecha_na) or fecha_na == "":
            print("Formato de fecha valida o fecha vacia")

            # Remuevo el mensaje de error si este existe
            self.master.vista_agregar_contacto.label_error.grid_remove()
            return True

        else:
            print('Formato de fecha invalida')
            self.master.vista_agregar_contacto.label_error.configure(
                text="Formato de fecha invalido")
            self.master.vista_agregar_contacto.label_error.grid(
                column=0, row=6, pady=(40, 0), padx=40)
            return False

    def cancelar(self):
        """
        Regresa al menu principal al cancelara la operacion
        """
        self.master.vista_agregar_contacto.label_error.grid_remove()
        self.master.cambiar_frame(self.master.vista_inicio)

    def mostrar_contacto(self, nombre, numero, pais, fecha_na):
        """
        Sirve para ver el contacto agregado
        """
        self.master.cambiar_frame(self.master.vista_contacto)
        self.master.vista_contacto.controlador.mostrar_datos(
            nombre, numero, pais, fecha_na)
