from typing import Optional, Tuple, Union
import customtkinter

WIDTH = 40
HEIGHT = 20


class VistaAgregarContacto(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.columnconfigure(0, weight=1)
        self.entrada = {}
        self.boton = {}

        # Div para oopcciones
        self.div_form = customtkinter.CTkFrame(self, )

        # Inicializando comandos
        self.inicializar()

        # Entrada de Nombre
        self.entrada['nombre'] = customtkinter.CTkEntry(
            self, width=master.WIDTH, placeholder_text="Nombre")
        self.entrada['nombre'].grid(
            column=0, row=0, padx=20, pady=(20, 0))

        # Entrada de Numero
        self.entrada['numero'] = customtkinter.CTkEntry(
            self, width=master.WIDTH, placeholder_text="+55 5555 555555")
        self.entrada['numero'].grid(
            column=0, row=1, padx=20, pady=(20, 0))

        # Entrada de Pais
        self.entrada['pais'] = customtkinter.CTkEntry(
            self, width=master.WIDTH, placeholder_text="Pais")
        self.entrada['pais'].grid(
            column=0, row=2, padx=20, pady=(20, 0))

        # Entrada Fecha Nacimiento
        self.entrada['fecha_na'] = customtkinter.CTkEntry(
            self, width=master.WIDTH, placeholder_text="Fecha Nacimiento aaaa-mm-dd")
        self.entrada['fecha_na'].grid(
            column=0, row=3, padx=20, pady=(20, 0))

        # Boton Guardar
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=master.WIDTH, height=HEIGHT, text="Guardar", command=self.insertar_datos)
        self.boton__agregar_contacto.grid(
            row=4, column=0, padx=20, pady=(20, 0))

        # Boton Cancelar
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=master.WIDTH, height=HEIGHT, text="Cancelar", command=self.cancelar)
        self.boton__agregar_contacto.grid(
            row=5, column=0, padx=20, pady=(20, 0))

        # Mostrar errores
        self.label_error = customtkinter.CTkLabel(self, fg_color='red')

    def inicializar(self):
        # Crear consulta de inserccion
        self.insertar_datos = self.controlador.insertar_datos

        # Funcion que limpia los campos
        self.limpiar_campos = self.controlador.limpiar_campos

        # Funcion para volver menu principal
        self.cancelar = self.controlador.cancelar
