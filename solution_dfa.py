from automata.fa.dfa import DFA

acceptedAlphabet = {'0', '1'}

# AFD para L1: { w ∈ E* | w termina em 010 }
dfa_l1 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q0'},
        'q3': {'0': 'q1', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q3'}
)

# AFD para L2: { w ∈ E* | w contém três zeros consecutivos }
dfa_l2 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q3', '1': 'q0'},
        'q3': {'0': 'q3', '1': 'q3'}
    },
    initial_state='q0',
    final_states={'q3'}
)

# AFD para L3: { w ∈ E* | w tem um número par de 0's }
dfa_l3 = DFA(
    states={'q0', 'q1'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q0', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q0'}
)

# AFD para L4: { w ∈ E* | w não contém três zeros consecutivos }
dfa_l4 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q3', '1': 'q0'},
        'q3': {'0': 'q3', '1': 'q3'}
    },
    initial_state='q0',
    final_states={'q0', 'q1', 'q2'}
)

# AFD para L5: { w ∈ E* | w tem um número ímpar de 1's }
dfa_l5 = DFA(
    states={'q0', 'q1'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q1'}
)

# AFD para L6: { w ∈ E* | w contém um múltiplo de 5 ocorrências de 1's }
dfa_l6 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q3'},
        'q3': {'0': 'q3', '1': 'q4'},
        'q4': {'0': 'q4', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q0'}
)

# AFD para L7: { w ∈ E* | w contém '00' ou '11' como substring }
dfa_l7 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols=acceptedAlphabet,
    transitions={
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q3', '1': 'q2'},
        'q2': {'0': 'q1', '1': 'q3'},
        'q3': {'0': 'q3', '1': 'q3'}
    },
    initial_state='q0',
    final_states={'q3'}
)


# Função para testar os AFDs
def test_dfa(dfa, words):
    for word in words:
        result = dfa.accepts_input(word)
        print(f'Palavra: {word}, Sequência válida: {result}')


# Casos de teste para cada AFD
test_words = ['010', '0001', '0101', '000', '11111', '1101']

print("====== Testando AFD para L1 -> { w ∈ E* | w termina em 010 } ======")
test_dfa(dfa_l1, test_words)

print(
    "\n====== Testando AFD para L2 -> { w ∈ E* | w contém três zeros consecutivos } ======")
test_dfa(dfa_l2, test_words)

print(
    "\n====== Testando AFD para L3 -> { w ∈ E* | w tem um número par de 0's } ======")
test_dfa(dfa_l3, test_words)

print(
    "\n====== Testando AFD para L4 -> { w ∈ E* | w não contém três zeros consecutivos } ======")
test_dfa(dfa_l4, test_words)

print(
    "\n====== Testando AFD para L5 -> { w ∈ E* | w tem um número ímpar de 1's } ======")
test_dfa(dfa_l5, test_words)

print(
    "\n====== Testando AFD para L6 -> { w ∈ E* | w contém um múltiplo de 5 ocorrências de 1's } ======")
test_dfa(dfa_l6, test_words)

print(
    "\n====== Testando AFD para L7 -> { w ∈ E* | w contém '00' ou '11' como substring } ======")
test_dfa(dfa_l7, test_words)
