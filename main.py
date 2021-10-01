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
Credito = ["410180","410181","441310","441311","455508","455525","455526","455527","455529","455504","455500","455503","455505","455508","455513","455540","455545","542010","544551",
"417155","457156","493160","493161","493162","547086","547077","547095","542977","544053","455502","418073","494398","416502","456880","491280","491281","491283","491284","491294",
"491295","540956","541278","541286","541290","547068","547074","547092","426012","413405","413406","522174","452421","473701","404360","462974","404360","402029","446565","404903",
"431479","420199","421811","463186","512795","854881","881006","881052","530756","854899","518899","547093","454492","529091","491272","498460","455255","549138","548234","439120",
"547112","491501","528875","544672","491271","454069","454057","410852","528851","528843","441541","435741","542537","522130","512823","520213","512809","491502","529001","529088",
"490178","490176","547075","528866","493165","493164","518853","528804","528877","545039","525424","420713","559209","520608","405306","528805","518004","402318","402582","425981",
"554764","512745","491512","491572","491573","493135","493136","494133","494134","540845","545307","547015","547046","547146","547157","554900","491871","491872","544204","545375",
"491346","491343","547080","491341","491366","491371","491586","493157","493172","493173","544548","544549","547078","547079","547096","547097","491375","493158","370700","370701",
"370702","370703","370704","370705","370706","370707","370708","370709","370710","370711","370712","370713","370714","370715","370716","370717","370718","370719","370720","370721",
"370722","370723","370724","370725","370726","370727","370728","370729","370730","370731","370732","370733","370734","370735","370736","370737","370738","370739","370740","370741",
"370742","370743","370744","370745","370746","370747","370748","370749","370750","370751","370752","370753","370754","370755","370756","370757","370758","370759","370760","370761",
"370762","370763","370764","370765","370766","370767","370768","370769","370770","370771","370772","370773","370774","370775","370776","370777","370778","370779","370780","370781",
"370782","370783","370784","370785","370786","370787","370788","370789","370790","370791","370792","370793","370794","370795","370796","370797","370798","370799","376600","376601",
"376602","376603","376604","376605","376606","376607","376608","376609","376610","376611","376612","376613","376614","376615","376616","376617","376618","376619","376620","376621",
"376622","376623","376624","376625","376626","376627","376628","376629","376630","376631","376632","376633","376634","376635","376636","376637","376638","376639","376640","376641",
"376642","376643","376644","376645","376646","376647","376648","376649","376650","376651","376652","376653","376654","376655","376656","376657","376658","376659","376660","376661",
"376662","376663","376664","376665","376666","376667","376668","376669","376670","376671","376672","376673","376674","376675","376676","376677","376678","376679","376680","376681",
"376682","376683","376684","376685","376686","376687","376688","376689","376690","376691","376692","376693","376694","376695","376696","376697","376698","376699","376700","376701",
"376702","376703","376704","376705","376706","376707","376708","376709","376710","376711","376712","376713","376714","376715","376716","376717","376718","376719","376720","376721",
"376722","376723","376724","376725","376726","376727","376728","376729","376730","376731","376732","376733","376734","376735","376736","376737","376738","376739","376740","376741",
"376742","376743","376744","376745","376746","376747","376748","376749","376750","376751","376752","376753","376754","376755","376756","376757","376758","376759","376760","376761",
"376762","376763","376764","376765","376766","376767","376768","376769","376770","376771","376772","376773","376774","376775","376776","376777","376778","376779","376780","376781",
"376782","376783","376784","376785","376786","376787","376788","376789","376790","376791","376792","376793","376794","376795","376796","376797","376798","376799","377600","377601",
"377602","377603","377604","377605","377606","377607","377608","377609","377610","377611","377612","377613","377614","377615","377616","377617","377618","377619","377620","377621",
"377622","377623","377624","377625","377626","377627","377628","377629","377630","377631","377632","377633","377634","377635","377636","377637","377638","377639","377640","377641",
"377642","377643","377644","377645","377646","377647","377648","377649","377650","377651","377652","377653","377654","377655","377656","377657","377658","377659","377660","377661",
"377662","377663","377664","377665","377666","377667","377668","377669","377670","377671","377672","377673","377674","377675","377676","377677","377678","377679","377680","377681",
"377682","377683","377684","377685","377686","377687","377688","377689","377690","377691","377692","377693","377694","377695","377696","377697","377698","377699"]

Credito_8 = ["45552925","45552927","54705050","54709681"]

#Variables

#Funciones
def get_cadena():
    #print(entry.get())
    automataExist=aut("tarjeta_existente.txt")
    automataVisa=aut("comprobar_visa.txt")
    automataMaster=aut("comprobar_mastercard.txt")
    cadena=""
    #print(automataObj.beginValidate(entry.get()))
    if(automataExist.beginValidate(entry.get())==True):
        cadena=cadena+"Tarjeta"
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if(automataVisa.beginValidate(entry.get())):
            cadena=cadena+" Visa"
        elif(automataMaster.beginValidate(entry.get())):
            cadena=cadena+" Mastercard"
        else:
            cadena=cadena+" Diferente"
        
        if(entry.get()[0:6] in Credito or entry.get()[0:6] in Credito_8):
            cadena=cadena +" Credito"
        else:
            cadena=cadena +" Debito"
        datos_label = tkinter.Label(window, text=cadena, font=('Impact', 17), bg="#A6D6D6").place(x=325, y=510)

    else:
        datos_label_2 = tkinter.Label(
    window, text="Numero no Valido", font=('Impact', 14), bg="#A6D6D6").place(x=320, y=510)


#Labels y botones
datos_label = tkinter.Label(
    window, text="Inserte una cadena con grafo importado", font=('Impact', 16), bg="#A6D6D6").place(x=235, y=0)

get_button = tkinter.Button(window, text="Validar cadena", font=(
    'Lucida Console', 10), bg="#537EC5", borderwidth=5, relief="raised", command=get_cadena).place(x=446, y=42, width=125, height=36)


window.mainloop()
   
