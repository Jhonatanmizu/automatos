from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


def dfa_to_nfa(dfa: DFA) -> NFA:
    """
    Converts a Deterministic Finite Automaton (DFA) into an equivalent Nondeterministic Finite Automaton (NFA).

    :param dfa: An instance of DFA.
    :return: An equivalent NFA.
    """
    # Copy DFA attributes to create an NFA
    nfa_transitions = {
        state: {symbol: {target} for symbol, target in transitions.items()}
        for state, transitions in dfa.transitions.items()
    }

    return NFA(
        states=dfa.states,
        input_symbols=dfa.input_symbols,
        transitions=nfa_transitions,
        initial_state=dfa.initial_state,
        final_states=dfa.final_states
    )


# Example DFA for testing
dfa_example = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q0', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)


# Convert the example DFA to an NFA
nfa_converted = dfa_to_nfa(dfa_example)

# Test the converted NFA
print("Converted NFA:")
print(f"States: {nfa_converted.states}")
print(f"Input Symbols: {nfa_converted.input_symbols}")
print(f"Transitions: {nfa_converted.transitions}")
print(f"Initial State: {nfa_converted.initial_state}")
print(f"Final States: {nfa_converted.final_states}")

# Validate the converted NFA
print(f"Is the NFA valid? {nfa_converted.validate()}")
