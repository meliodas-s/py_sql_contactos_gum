import customtkinter

WIDTH_BOTON = 40
HEIGHT_BOTON = 20


class VistaInicio(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.columnconfigure(0, weight=1)
        
        # Inicializando controlador
        self.inicializar()

        # Boton Agregar Contacto
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=WIDTH_BOTON, height=HEIGHT_BOTON, text="Agregar contacto", command=self.agregar_contactos)
        self.boton__agregar_contacto.grid(
            row=0, column=0, sticky="we", padx=20, pady=(20,0))

        # Boton Ver contactos
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=WIDTH_BOTON, height=HEIGHT_BOTON, text="Ver contactos", command=self.ver_contactos)
        self.boton__agregar_contacto.grid(
            row=2, column=0, sticky="we", padx=20, pady=(20,0))

    def inicializar(self):
        """
        Se encarga de cargar comandos para cambiar de pestañas, entre otros
        """
        
        # Agregar Contacto
        self.agregar_contactos = self.controlador.agregar_contactos

        # Ver contactos
        self.ver_contactos = self.controlador.ver_contactos
