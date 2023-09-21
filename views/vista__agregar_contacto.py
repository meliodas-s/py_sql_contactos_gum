from typing import Optional, Tuple, Union
import customtkinter

WIDTH_BOTON = 40
HEIGHT_BOTON = 20


class VistaAgregarContacto(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.columnconfigure(0, weight=1)
        self.entrada = {}
        self.boton = {}

        # Inicializando comandos

        # Entrada de Nombre
        self.entrada['nombre'] = customtkinter.CTkEntry(
            self, placeholder_text="Nombre")
        self.entrada['nombre'].grid(
            column=0, row=0, sticky="we", padx=20, pady=(20, 0))

        # Entrada de Numero
        self.entrada['numero'] = customtkinter.CTkEntry(
            self, placeholder_text="Numero")
        self.entrada['numero'].grid(
            column=0, row=1, sticky="we", padx=20, pady=(20, 0))

        # Entrada de Pais
        self.entrada['pais'] = customtkinter.CTkEntry(
            self, placeholder_text="Pais")
        self.entrada['pais'].grid(
            column=0, row=2, sticky="we", padx=20, pady=(20, 0))

        # Entrada Fecha Nacimiento
        self.entrada['fecha_na'] = customtkinter.CTkEntry(
            self, placeholder_text="Fecha Nacimiento")
        self.entrada['fecha_na'].grid(
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

    def inicializar(self):
        # Crear consulta de inserccion
        self.insertar_datos = self.controlador.insertar_datos
        
        # Funcion que limpia los campos
        self.limpiar_campos = self.controlador.limpiar_campos
        
        # Funcion para volver menu principal
        

