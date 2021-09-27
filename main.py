from tkinter import *
import tkinter.filedialog
from tkinter.constants import END
from tkinter import filedialog
from tkinter import Frame, Toplevel, ttk
from typing import Text
from automata import automata as aut

# Creación de la ventana
window = tkinter.Tk()
window.title("DFA verbo jugar")
window.geometry("800x600")
window.resizable(False, False)
window.config(bg="#A6D6D6")
# Creación del Frame del grafo
frame = Frame(window)
frame.place(x=70, y=125)
frame.config(bg="#126e82", borderwidth=5, relief="raised")
frame.config(width=650, height=382)
#Imagen del grafo
#diagrama_img = tkinter.PhotoImage(file="source/grafo_frame.png")
#diagrama_button = tkinter.Label(
#    window, image=diagrama_img, borderwidth=0, bg="#126e82").place(x=70, y=125, width=650, height=382)
# Crear caja de texto.
entry = ttk.Entry(window,font=('Lucida Console', 10))
# Posicionarla en la ventana.
entry.place(x=220, y=50,width=200, height=26)
#Insertar texto
cadena = ""
entry.insert(0,cadena)

#Variables

#Funciones
def get_cadena():
    print(entry.get())
    automataObj=aut()
    print(automataObj.beginValidate(entry.get()))
    if(automataObj.beginValidate(entry.get())==True):
        datos_label = tkinter.Label(
    window, text="Cadena Valida", font=('Impact', 17), bg="#A6D6D6").place(x=325, y=510)
    else:
        datos_label_2 = tkinter.Label(
    window, text="Cadena no Valida", font=('Impact', 14), bg="#A6D6D6").place(x=320, y=510)


#Labels y botones
datos_label = tkinter.Label(
    window, text="Inserte una cadena con grafo importado", font=('Impact', 16), bg="#A6D6D6").place(x=235, y=0)

get_button = tkinter.Button(window, text="Validar cadena", font=(
    'Lucida Console', 10), bg="#537EC5", borderwidth=5, relief="raised", command=get_cadena).place(x=446, y=42, width=125, height=36)


window.mainloop()