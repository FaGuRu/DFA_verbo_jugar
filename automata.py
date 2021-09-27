class automata:

    S = []
    Q = []
    F = []
    q0=""
    D = {}

    def beginValidate(self,cadena):
        global Q,S,F,q0,D
        D = {}
        entrada = open("entrada.txt", "r")
        line = entrada.readline()
        auxS = line[line.find('{')+1:line.find('}')]
        S=auxS.split(',')
        line = entrada.readline()
        auxQ = line[line.find('{')+1:line.find('}')]
        Q=auxQ.split(',')
        line = entrada.readline()
        auxF = line[line.find('{')+1:line.find('}')]
        F=auxF.split(',')
        line = entrada.readline()
        #print(line)
        auxD = line[line.find('{')+1:line.find(')}')]
        auxD=auxD.replace('),(',';')
        auxD=auxD.replace('(','')
        auxArrayD=auxD.split(';')
        print(auxArrayD)
        if ',{' in auxD: #Metodo AFD
            for i in range(len(auxArrayD)):
                auxStringStates=auxArrayD[i][:auxArrayD[i].find(',{')] 
                auxArrayStringStates=auxStringStates.split(',')
                tupleStates=(auxArrayStringStates[0],auxArrayStringStates[1])
                auxString=auxArrayD[i][auxArrayD[i].find('{')+1:auxArrayD[i].find('}')]
                #print(tupleStates)
                auxArrayString=auxString.split(',')
                D[tupleStates]=auxArrayString
        else: #Metodo FNA
            for i in range(len(auxArrayD)):
                auxArrayStringStates=auxArrayD[i].split(',')
                tupleStates=(auxArrayStringStates[0],auxArrayStringStates[1])
                D[tupleStates]=auxArrayStringStates[2]
                

            print(auxArrayStringStates)
                

        line = entrada.readline()
        q0 = line[line.find('=')+2:]
        
        return self.validate(cadena,q0)

    def validate(self,  cadena, actualState):
        if cadena == '':
            return actualState in F
        else:
            symbol = cadena[0:1]
            # print(symbol)
            # print(cadena)
            # print(D)
            if(actualState, symbol) in D:
                new_cadena = cadena[1:]
                #print(new_cadena)
                transitions = D[(actualState, symbol)]
                #print(transitions)
                for transition in transitions:
                    if self.validate(new_cadena, transition):
                        return True
            return False
        
    