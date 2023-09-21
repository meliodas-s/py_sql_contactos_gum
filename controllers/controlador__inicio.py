class ControladorInicio:
    def __init__(self, master) -> None:
        self.master = master

    def agregar_contactos(self):
        self.master.cambiar_frame(self.master.vista_agregar_contacto)

    def ver_contactos(self):
        return 0
