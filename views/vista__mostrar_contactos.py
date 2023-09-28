import customtkinter


class VistaMostrarContactos(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Llamar datos sqlite
        self.contactos = self.controlador.llamar_datos()

        # Frame scroleable
        self.div_scrol = customtkinter.CTkScrollableFrame(
            self, label_text='Contactos', width=700)
        self.div_scrol.grid(column=0, row=0, sticky='ns')
        self.div_scrol.columnconfigure(0, weight=1)

        self.ultimo_contacto = 0
        # Lista de contactos con (boton ver)
        for i, contacto in enumerate(self.contactos):
            self.incializar_contactos(contacto[0], contacto[1], i)
            self.ultimo_contacto += 1

    def incializar_contactos(self, id, nombre, pocision):
        """
        Descripcion:
            Agrega los contactos a la vista de contactos, junto a un boton 'ver' para ver toda la informacion.

        Args:
            nombre (str) : Nombre ingresado
            id (int) : id generado por sqlite
            pocision (int) : Fila donde va ubicado

        Returns:
            void : No regresa nada
        """
        # Frame para el contacto y boton
        frame_contact = customtkinter.CTkFrame(self.div_scrol)
        frame_contact.grid(row=pocision, column=0, sticky='we', pady=10)
        frame_contact.columnconfigure(0, weight=80)
        frame_contact.columnconfigure(1, weight=20)
        frame_contact.rowconfigure(0, weight=1)

        # Info reducida del contacto
        nombre_contact = customtkinter.CTkLabel(
            frame_contact, text=f'Nombre: {nombre}')
        nombre_contact.grid(column=0, row=0)

        # Boton para ver el contacto
        boton = customtkinter.CTkButton(
            frame_contact, text='Ver', command=self.to_vista_contacto(id))
        boton.grid(column=1, row=0)

    def nuevo_contacto(self, nuevo_id):
        """
        Descripcion:
            Actualiza los contactos cuando se agrega uno nuevo. Conecta con sql y lo crea.

        Args:
            self (VistaMostrarContactos) : Objeto dueño del metodo.
            nuevo_id (int) : Id con el que se realiza la consulta.

        Returns:
            void : No se retorna nada aun. Podria ser un booleano para corroborar que todo salio bien.
        """
        contacto = self.controlador.llamar_contacto_especifico_con_id(nuevo_id)[0]
        self.incializar_contactos(
            contacto[0], contacto[1], self.ultimo_contacto + 1)
        self.ultimo_contacto += 1
        return 0

    def to_vista_contacto(self, id):
        """
        Dado un id, devuelve una lambda funcion que permite mostrar ese contacto
        """
        def entrar_contacto(id=id):
            # Coneccion sqlite3, consulta contacto id, cerrar conn
            import sqlite3
            conn = sqlite3.connect('./data/contactos.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM contactos WHERE ID = ?', (id,))

            resultado = cursor.fetchall()[0]
            cursor.close()

            self.master.vista_contacto.controlador.mostrar_datos(
                resultado[1], resultado[2], resultado[3], resultado[4])
            self.master.cambiar_frame(self.master.vista_contacto)
        return entrar_contacto
