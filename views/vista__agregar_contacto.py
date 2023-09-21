from typing import Optional, Tuple, Union
import customtkinter

WIDTH_BOTON = 40
HEIGHT_BOTON = 20

class VistaAgregarContacto(customtkinter.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color,
                         border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        # Entrada de Nombre
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Nombre")
        self.entrada__nombre.grid(
            column=0, row=0, sticky="we", padx=20, pady=(20, 0))

        # Entrada de Numero
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Numero")
        self.entrada__nombre.grid(
            column=0, row=0, sticky="we", padx=20, pady=(20, 0))

        # Entrada de Pais
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Pais")
        self.entrada__nombre.grid(
            column=0, row=0, sticky="we", padx=20, pady=(20, 0))

        # Entrada Fecha Nacimiento
        self.entrada__nombre = customtkinter.CTkEntry(
            self, placeholder_text="Fecha Nacimiento")
        self.entrada__nombre.grid(
            column=0, row=0, sticky="we", padx=20, pady=(20, 0))
        
        # Boton Guardar
        self.boton__agregar_contacto = customtkinter.CTkButton(
            self, width=WIDTH_BOTON, height=HEIGHT_BOTON, text="Guardar", command=self.insertar_datos)
        self.boton__agregar_contacto.grid(
            row=0, column=0, sticky="we", padx=20, pady=(20,0))


        # Boton Cancelar

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
