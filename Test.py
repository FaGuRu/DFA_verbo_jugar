from automata.fa.dfa import DFA

dfa = DFA(
    states = {'q0','q1'},
    input_symbols = {'0','1','2','3','4','5','6','7','8','9','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'},
    transitions = {
        'q0':{'l':'q1'},
        'q1':{'l':'q1'},
        'q1':{'d':'q1'},
    },
    initial_state = 'q0',
    final_states= {'q2'}
)

if(dfa.accepts_input('_variant')):
    print('Cadena valida')
else:
    print('Cadena no valida')