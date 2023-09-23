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
        self.div_scrol.grid(column = 0, row=0, sticky = 'ns')
        self.div_scrol.columnconfigure(0,weight=1)

        # Lista de contactos con (boton ver)
        i = 0
        for contacto in self.contactos:
            # Frame para el contacto y boton
            frame_contact = customtkinter.CTkFrame(self.div_scrol)
            frame_contact.grid(row=i, column=0, sticky='we', pady=10)
            frame_contact.columnconfigure(0, weight=80)
            frame_contact.columnconfigure(1, weight=20)
            frame_contact.rowconfigure(0, weight=1)

            # Info reducida del contacto
            nombre_contact = customtkinter.CTkLabel(
                frame_contact, text=f'Nombre: {contacto[1]}')
            nombre_contact.grid(column=0, row=0)

            # Boton para ver el contacto
            boton = customtkinter.CTkButton(
                frame_contact, text='Ver', command=self.to_vista_contacto(contacto[0]))
            boton.grid(column=1, row=0)

            i += 1

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
