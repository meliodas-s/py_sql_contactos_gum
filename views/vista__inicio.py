import customtkinter

class VistaInicio(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador

    # Agregar Contacto
    def agregar_contactos(self):
        """
        Cambia hacia VistaAgregarContacto
        """
        return 0
    
    # Ver contactos
    def ver_contactos(self):
        """
        Cambia hacia VistaVerContacto. Esta ACTUALIZA y ELIMINA contactos.
        """
        # Actualizar contacto

        # Eliminar contacto
        return 0
