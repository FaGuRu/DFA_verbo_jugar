from tkinter import *
import tkinter.filedialog
from tkinter.constants import END
from tkinter import filedialog
from tkinter import Frame, Toplevel, ttk
from typing import Text

# Creación de la ventana
window = tkinter.Tk()
window.title("DFA verbo jugar")
window.geometry("800x600")
window.resizable(False, False)
window.config(bg="#A6D6D6")

# Crear caja de texto.
entry = ttk.Entry(window,font=('Lucida Console', 10))
# Posicionarla en la ventana.
entry.place(x=310, y=50,width=200, height=26)
#Insertar texto
cadena = ""
entry.insert(0,cadena)

#Variables

#Funciones
def get_cadena():
    print(entry.get())
    #entry.delete(0,cadena)

#Labels y botones
datos_label = tkinter.Label(
    window, text="Inserte una cadena con el verbo Jugar", font=('Impact', 16), bg="#A6D6D6").place(x=240, y=0)

get_button = tkinter.Button(window, text="Validar cadena", font=(
    'Lucida Console', 10), bg="#537EC5", borderwidth=5, relief="raised", command=get_cadena).place(x=346, y=90, width=125, height=36)

window.mainloop()