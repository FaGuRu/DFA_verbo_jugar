class automata:
    num_estados = 0
    estados = []
    cardinalidad = []
    alfabeto = []
    estado_inicial = ""
    estado_final = []
    transicion = []
    
    def get_automata(self,cadena_valida_):
        valido = False
        lista = []
        start = self.estados[0]
        cadena_valida = cadena_valida_
        
        for symbol in cadena_valida:
            lista.append(self.transicion[self.estados.index(start)][self.alphabet.index(symbol)])
            start = self.transicion[self.estados.index(start)][self.alphabet.index(symbol)]
            
        for final in self.estado_final:
            if (lista[-1]--final):
                valido = True
        
        return valido
       
        
    