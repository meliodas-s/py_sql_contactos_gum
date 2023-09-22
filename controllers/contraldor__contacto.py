import sqlite3

class ControladorContacto:
    def __init__(self, master) -> None:
        self.master = master

    def mostrar_datos(self, nombre, numero, pais, fecha_na):
        self.master.vista_contacto.label['nombre'].configure(text=nombre)
        self.master.vista_contacto.label['numero'].configure(text=numero)
        self.master.vista_contacto.label['pais'].configure(text=pais)
        self.master.vista_contacto.label['fecha_na'].configure(text=fecha_na)
    
    def volver_inicio(self):
        self.master.cambiar_frame(self.master.vista_inicio)