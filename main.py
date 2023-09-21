from typing import Optional, Tuple, Union
import customtkinter

# Importando Vistas
from views.vista__inicio import VistaInicio
from views.vista__agregar_contacto import VistaAgregarContacto
from views.vista__contacto import VistaContacto

# Importando Controladores
from controllers.controlador__inicio import ControladorInicio
from controllers.controlador__agregar_contacto import ControladorAgregarContacto
from controllers.contraldor__contacto import ControladorContacto


class Aplicacion(customtkinter.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # Configuraciones basicas
        self.title("Titulo")
        self.geometry("500x700")
        self.minsize(400, 600)
        self.maxsize(500, 700)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Llamar vista principal
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        # VistaInicio
        controlador_inicio = ControladorInicio(self)
        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.ajustar_frame(self.vista_inicio)

        # VistaAgregarContacto
        controlador_agregar_contacto = ControladorAgregarContacto(self)
        self.vista_agregar_contacto = VistaAgregarContacto(
            self, controlador_agregar_contacto)
        self.ajustar_frame(self.vista_agregar_contacto)

        # VistaContacto
        controlador_contacto = ControladorContacto(self)
        self.vista_contacto = VistaContacto(self, controlador_contacto)
        self.ajustar_frame(self.vista_contacto)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky='nswe')

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
