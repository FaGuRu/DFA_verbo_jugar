class automata:

    S = []
    Q = []
    F = []
    q0=""
    D = {}
    nombreAutomata=""

    def __init__(self,nombreTxt):
        self.nombreAutomata=nombreTxt
        


    def beginValidate(self,cadena):
        global Q,S,F,q0,D
        D = {}
        print("Iniciando validacion")
        entrada = open(self.nombreAutomata, "r")
        line = entrada.readline()
        auxS = line[line.find('{')+1:line.find('}')]
        auxS=auxS.replace(' ','')
        
        S=auxS.split(',')
        line = entrada.readline()
        auxQ = line[line.find('{')+1:line.find('}')]
        auxQ=auxQ.replace(' ','')
        Q=auxQ.split(',')
        line = entrada.readline()
        auxF = line[line.find('{')+1:line.find('}')]
        auxF=auxF.replace(' ','')
        F=auxF.split(',')
        line = entrada.readline()
        #print(line)
        #print(auxS)
        #print(auxQ)
        #print(auxF)
        auxD = line[line.find('{')+1:line.find(')}')]
        auxD=auxD.replace(', ,','epsilon')
        auxD=auxD.replace(' ','')
        #print(repr(auxD))
        auxD=auxD.replace('),(',';')
        auxD=auxD.replace('(','')
        auxD=auxD.replace('epsilon',', ,')
        #print(auxD)
        auxArrayD=auxD.split(';')
        #print(auxArrayD)
        if ',{' in auxD: #Metodo AFD
            print('AFD')
            for i in range(len(auxArrayD)):
                auxStringStates=auxArrayD[i][:auxArrayD[i].find(',{')] 
                auxArrayStringStates=auxStringStates.split(',')
                tupleStates=(auxArrayStringStates[0],auxArrayStringStates[1])
                auxString=auxArrayD[i][auxArrayD[i].find('{')+1:auxArrayD[i].find('}')]
                #print(tupleStates)
                auxArrayString=auxString.split(',')
                D[tupleStates]=auxArrayString
        else: #Metodo FNA
            print('FNA')
            for i in range(len(auxArrayD)):
                auxArrayStringStates=auxArrayD[i].split(',')
                tupleStates=(auxArrayStringStates[0],auxArrayStringStates[1])
                auxArrayString=auxArrayStringStates[2].split(',')
                D[tupleStates]=auxArrayString
                

            #print(auxArrayStringStates)
                

        line = entrada.readline()
        line=line.replace('{','')
        line=line.replace('}','')
        line=line.replace(' ','')
        q0 = line[line.find('=')+1:]
        
        return self.validate(cadena,q0)

    def validate(self,  cadena, actualState):
        print(self.nombreAutomata)
        if cadena == '':
            print("finalizada")
            return actualState in F
        else:
            symbol = cadena[0:1]
            # print(symbol)
            # print(cadena)
            # print(actualState)
            print(D)
            if(actualState, symbol) in D:
                new_cadena = cadena[1:]
                print(new_cadena)
                transitions = D[(actualState, symbol)]
                print(transitions)
                for transition in transitions:
                    if self.validate(new_cadena, transition):
                        return True
            return False


# def main():
#     # aut = automata()
#     # #aut(aut.beginValidate('1001'))


# if __name__ == "__main__":
#     main()