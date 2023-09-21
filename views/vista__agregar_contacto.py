from typing import Optional, Tuple, Union
import customtkinter

WIDTH_BOTON = 40
HEIGHT_BOTON = 20


class VistaAgregarContacto(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.columnconfigure(0, weight=1)

        # Inicializando comandos

        # Entrada de Nombre
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Nombre")
        self.entrada__nombre.grid(
            column=0, row=0, sticky="we", padx=20, pady=(20, 0))

        # Entrada de Numero
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Numero")
        self.entrada__nombre.grid(
            column=0, row=1, sticky="we", padx=20, pady=(20, 0))

        # Entrada de Pais
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Pais")
        self.entrada__nombre.grid(
            column=0, row=2, sticky="we", padx=20, pady=(20, 0))

        # Entrada Fecha Nacimiento
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Fecha Nacimiento")
        self.entrada__nombre.grid(
            column=0, row=3, sticky="we", padx=20, pady=(20, 0))

        # Boton Guardar
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=WIDTH_BOTON, height=HEIGHT_BOTON, text="Guardar", command=self.insertar_datos)
        self.boton__agregar_contacto.grid(
            row=4, column=0, sticky="we", padx=20, pady=(20, 0))

        # Boton Cancelar
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=WIDTH_BOTON, height=HEIGHT_BOTON, text="Cancelar", command=self.insertar_datos)
        self.boton__agregar_contacto.grid(
            row=5, column=0, sticky="we", padx=20, pady=(20, 0))

    # Crear consulta de inserccion
    def insertar_datos(self):
        """
        Crea la consulta y la manda a la base de datos
        """
        return 0

    # Fncion que limpia los campos
    def limpiar_capos(self):
        """
        Limpiara los campos para proximas insercciones
        """
        return 0
