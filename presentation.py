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
        #self.parent.iconbitmap('assets\\Escudo_Alumni_Casilda.jpg')

        # Background image 
        self.parent.bg_photo = bg_photo = tk.PhotoImage(file='NatacionApp\\assets\\fondo.png')
        canvas = tk.Canvas(self.parent, width=700, height=400)   
        canvas.create_image(0, 0, image=bg_photo,anchor="nw" )      
        canvas.create_text(350, 100, text="Natación APP", font=("Helvetica", 50), fill="white")
        canvas.pack(fill="both", expand=True)

        # Botones ventana principal
        btn_carga = tk.Button(self.parent, text="Carga de datos",font=("Helvetica", 12), width=20)
        canvas.create_window(255, 200, anchor="nw", window=btn_carga)

        btn_orden = tk.Button(self.parent, text="O.D. Recreativo", font=("Helvetica", 12), width=20)
        canvas.create_window(255, 250, anchor="nw", window=btn_orden)

        btn_orden = tk.Button(self.parent, text="O.D. Competitivo", font=("Helvetica", 12), width=20)
        canvas.create_window(255, 285, anchor="nw", window=btn_orden)

        btn_result = tk.Button(self.parent, text="Resultados", font=("Helvetica", 12), width=20)
        canvas.create_window(255, 330, anchor="nw", window=btn_result)

        self.parent.resizable(width=False, height=False)

        # Protocolo de cierre
        #self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

def main():
    APP = UI(parent=tk.Tk())
    APP.mainloop()
