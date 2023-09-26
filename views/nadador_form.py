"""Pantalla que contiene el formulario de carga de un nadador"""
import tkinter
from tkinter import ttk

def open_nadador_form():
    """Formulario de carga"""  
    window = tkinter.Toplevel()
    window.title("Carga de datos Nadador")
    window.geometry("700x400")

    frame = tkinter.Frame(window)
    frame.pack()

    def add_prueba_row():
        row_frame = tkinter.Frame(pruebas_info_frame)
        row_frame.grid(row=len(prueba_rows) + 2, column=0, sticky="news", padx=20, pady=5)

        prueba_label = tkinter.Label(row_frame, text="Prueba")
        prueba_entry = ttk.Combobox(row_frame, values=["Prueba 1", "Prueba 2", "Prueba 3"], 
                                    width=30)
        minutos_label = tkinter.Label(row_frame, text="mm")
        minutos_entry = tkinter.Entry(row_frame, width=5)
        segundos_label = tkinter.Label(row_frame, text="ss")
        segundos_entry = tkinter.Entry(row_frame, width=5)
        milisegundos_label = tkinter.Label(row_frame, text="sss")
        milisegundos_entry = tkinter.Entry(row_frame, width=5)

        eliminar_button = tkinter.Button(row_frame, text="Eliminar", command=lambda 
                                         row=row_frame: remove_prueba_row(row))

        prueba_label.grid(row=0, column=0)
        prueba_entry.grid(row=0, column=1, padx=30)
        minutos_label.grid(row=0, column=2)
        minutos_entry.grid(row=0, column=3)
        segundos_label.grid(row=0, column=4)
        segundos_entry.grid(row=0, column=5)
        milisegundos_label.grid(row=0, column=6)
        milisegundos_entry.grid(row=0, column=7)
        eliminar_button.grid(row=0, column=8, padx=20)

        prueba_rows.append(row_frame)

    def remove_prueba_row(row):
        row.destroy()
        prueba_rows.remove(row)

    # Define personal info frame
    nadador_info_frame = tkinter.LabelFrame(frame, text="Información Personal")
    nadador_info_frame.grid(row=0, column=0, padx=20, pady=20)

    # Define widgets
    name_label = tkinter.Label(nadador_info_frame, text="Nombre y Apellido")
    name_entry = tkinter.Entry(nadador_info_frame, width=30)
    sexo_label = tkinter.Label(nadador_info_frame, text="Sexo")
    sexo_combobox = ttk.Combobox(nadador_info_frame, values=['F', 'M'], width=5)
    categoria_label = tkinter.Label(nadador_info_frame, text="Categoria")
    categoria_entry = tkinter.Entry(nadador_info_frame, width=15)
    club_label = tkinter.Label(nadador_info_frame, text="Club")
    # reemplazar con endpoint
    club_entry = ttk.Combobox(nadador_info_frame, values=["Club1", "Club2"], width=30)

    # Define Grid
    name_label.grid(row=0, column=0)
    name_entry.grid(row=1, column=0)
    sexo_label.grid(row=0, column=1)
    sexo_combobox.grid(row=1, column=1)
    categoria_label.grid(row=0, column=2)
    categoria_entry.grid(row=1, column=2)
    club_label.grid(row=0, column=3)
    club_entry.grid(row=1, column=3)

    for widget in nadador_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #Define Pruebas frame
    pruebas_info_frame = tkinter.LabelFrame(frame)
    pruebas_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

    for widget in pruebas_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    prueba_rows = []

    add_prueba_button = ttk.Button(pruebas_info_frame, text="Añadir prueba", command=add_prueba_row)
    add_prueba_button.grid(row=0, column=0, pady=10)

    guardar_button = tkinter.Button(frame, text="Guardar")
    guardar_button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

    window.mainloop()

