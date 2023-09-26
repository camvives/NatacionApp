"""Pantalla de inicio de la aplicación"""
import tkinter as tk
from tkinter import PhotoImage
from . import nadador_form

def main():
    """Inicia la capa de presentación"""
    root = tk.Tk()

    bg_image = PhotoImage(file="C:\\Users\\camvi\\Documents\\natacionApp\\app\\NatacionApp\\assets\\fondo.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place( relwidth=1, relheight=1)
    label = tk.Label(root, text="NATACIÓN APP", font=("Helvetica", 30))
    label.place(relx=0.5, rely=0.5, anchor="center")

    menubar = tk.Menu(root)
    root.config(menu=menubar)
    root.geometry("800x450")

    menu_carga = tk.Menu(menubar, tearoff=False)
    menu_carga.add_command(label="Nadador", command=nadador_form.open_nadador_form)
    menu_carga.add_command(label="Prueba")
    menu_carga.add_command(label="Club")

    menu_edit = tk.Menu(menubar, tearoff=False)
    menu_edit.add_command(label="Nadadores")
    menu_edit.add_command(label="Pruebas")
    menu_edit.add_command(label="Clubes")

    menu_ord = tk.Menu(menubar, tearoff=False)
    menu_ord.add_command(label="Recreativo")
    menu_ord.add_command(label="Competitivo")

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_cascade(label="Carga de datos", menu=menu_carga)
    filemenu.add_cascade(label="Editar datos", menu=menu_edit)
    filemenu.add_separator()
    filemenu.add_cascade(label="Ordenamiento", menu=menu_ord)
    filemenu.add_separator()
    filemenu.add_command(label="Resultados")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)

    menubar.add_cascade(label="Archivo", menu=filemenu)

    root.mainloop()

if __name__ == "__main__":
    main()
