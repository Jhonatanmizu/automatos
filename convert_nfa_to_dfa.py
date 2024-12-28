from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def convert_nfa_to_dfa(nfa):
    """
    Convert a Non-Deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA).
    :param nfa: An NFA instance
    :return: A DFA instance
    """
    dfa = DFA.from_nfa(nfa)
    return dfa


# List of NFAs to convert and test
nfa_list = [
    (NFA(
        states={'q0', 'q1', 'q2', 'q3'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': {'q0'}, '1': {'q0', 'q1'}},
            'q1': {'0': {'q2'}},
            'q2': {'1': {'q3'}},
            'q3': {}
        },
        initial_state='q0',
        final_states={'q3'}
    ), "L1: Ends with 010"),
    (NFA(
        states={'q0', 'q1', 'q2', 'q3'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': {'q1'}, '1': {'q0'}},
            'q1': {'0': {'q2'}},
            'q2': {'0': {'q3'}},
            'q3': {'0': {'q3'}, '1': {'q3'}}
        },
        initial_state='q0',
        final_states={'q3'}
    ), "L2: Contains three consecutive zeros"),
    # Add other NFAs here following the same structure
]

# Process each NFA
for nfa, description in nfa_list:
    print(f"Processing {description}:")
    print(f"Validating NFA... {'Valid' if nfa.validate() else 'Invalid'}")
    dfa = convert_nfa_to_dfa(nfa)
    print(f"Converted DFA:")
    print(dfa)
