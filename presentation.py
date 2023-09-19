import tkinter as tk

class UI(tk.Frame):
    """Home screen"""

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """widgets for home screen"""
        self.parent.title("Natación APP")
        self.parent.iconbitmap('assets\\Escudo_Alumni_Casilda.jpg')

        # Background image 
        self.parent.bg_photo = bg_photo = tk.PhotoImage(file='assets\\fondo.jpg')
        canvas = tk.Canvas(self.parent, width=800, height=500)   
        canvas.create_image(0, 0, image=bg_photo,anchor="nw" )      
        canvas.create_text(400, 150, text="FaceMask Detector", font=("Helvetica", 50))
        canvas.pack(fill="both", expand=True)

        # Botones ventana principal
        btn_carga = tk.Button(self.parent, text="Carga de datos",font=("Helvetica", 15), width=20)
        canvas.create_window(170, 250, anchor="nw", window=btn_carga)

        btn_orden = tk.Button(self.parent, text="Ordenamiento de datos", font=("Helvetica", 12), width=20)
        canvas.create_window(300, 320, anchor="nw", window=btn_orden)

        btn_result = tk.Button(self.parent, text="Resultados", font=("Helvetica", 12), width=20)
        canvas.create_window(300, 320, anchor="nw", window=btn_result)

        # Protocolo de cierre
        #self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

def main():
    APP = UI(parent=tk.Tk())
    APP.mainloop()
