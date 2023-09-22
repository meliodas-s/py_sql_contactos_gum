import customtkinter
import sqlite3

from tkinter import PhotoImage
from PIL import Image, ImageTk


class VistaContacto(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        self.columnconfigure(0, weight=1)

        # Inicializar controlador
        self.inicializar()

        # Imagen del contacto
        image = Image.open("./images/01contacto.png").resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        self.image_label = customtkinter.CTkLabel(
            self, image=photo, text="", width=100, height=100)
        self.image_label.grid(column=0, row=0, pady=(20, 0), padx=20)

        # Nombre del contacto
        self.label['nombre'] = customtkinter.CTkLabel(self)
        self.label['nombre'].grid(column=0, row=1, pady=(20,0), padx=20)

        # Numero del contacto
        self.label['numero'] = customtkinter.CTkLabel(self)
        self.label['numero'].grid(column=0, row=2, pady=(20,0), padx=20)

        # Pais del contacto
        self.label['pais'] = customtkinter.CTkLabel(self)
        self.label['pais'].grid(column=0, row=3, pady=(20,0), padx=20)

        # FechaNacimiento del contacto
        self.label['fecha_na'] = customtkinter.CTkLabel(self)
        self.label['fecha_na'].grid(column=0, row=4, pady=(20,0), padx=20)

        # Boton Volver inicio
        self.boton_inicio = customtkinter.CTkButton(self, text="Volver", command=self.volver_inicio)
        self.boton_inicio.grid(column=0, row=5, pady=(20,0), padx=20)

    # def cargar_datos(self, nombre, numero, pais, fecha_na):

    def inicializar(self):
        """
        Volver a la pantalla de inicio
        """
        self.label = {}
        self.volver_inicio = self.controlador.volver_inicio
