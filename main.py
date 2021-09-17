from tkinter import *
from automata.fa.dfa import DFA
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
# Creación del Frame delárbol
frame = Frame(window)
frame.place(x=70, y=125)
frame.config(bg="#126e82", borderwidth=5, relief="raised")
frame.config(width=650, height=382)

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
    #print(entry.get())
    dfa = DFA(
    states = {'q0','q1','q2','q3'},
    input_symbols = {'0','1'},
    transitions = {
        'q0':{'0':'q3','1':'q1'},
        'q1':{'0':'q2','1':'q1'},
        'q2':{'0':'q2','1':'q1'},
        'q3':{'0':'q3','1':'q3'},
    },
    initial_state = 'q0',
    final_states= {'q2'}
)
    #print("esta es la cadena = "+ entry.get())
    if(dfa.accepts_input(entry.get())):
        print('Cadena valida')
        cadena_label = tkinter.Label(window, text="Cadena Valida", font=(
        'Lucida Console', 15), bg="#A6D6D6").place(x=300, y=550)
    else:
        print('Cadena no valida')
        cadena_label = tkinter.Label(window, text="Cadena no valida", font=(
        'Lucida Console', 15), bg="#A6D6D6").place(x=300, y=550)

#Labels y botones
datos_label = tkinter.Label(
    window, text="Inserte una cadena con el verbo Jugar", font=('Impact', 16), bg="#A6D6D6").place(x=240, y=0)

get_button = tkinter.Button(window, text="Validar cadena", font=(
    'Lucida Console', 10), bg="#537EC5", borderwidth=5, relief="raised", command=get_cadena).place(x=446, y=42, width=125, height=36)

window.mainloop()