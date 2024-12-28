from collections import defaultdict
from itertools import chain


class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.start_state = None
        self.accept_states = set()
        self.transitions = defaultdict(lambda: defaultdict(set))

    def add_state(self, state, is_start=False, is_accept=False):
        self.states.add(state)
        if is_start:
            self.start_state = state
        if is_accept:
            self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        self.transitions[from_state][symbol].add(to_state)
        self.alphabet.add(symbol)


class DFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.start_state = None
        self.accept_states = set()
        self.transitions = {}

    def add_state(self, state, is_start=False, is_accept=False):
        self.states.add(state)
        if is_start:
            self.start_state = state
        if is_accept:
            self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        self.transitions[(from_state, symbol)] = to_state
        self.alphabet.add(symbol)


def nfa_to_dfa(nfa):
    dfa = DFA()

    # Map NFA state sets to DFA states
    state_map = {}

    def get_dfa_state(nfa_states):
        frozen = frozenset(nfa_states)
        if frozen not in state_map:
            dfa_state = f"Q{len(state_map)}"
            state_map[frozen] = dfa_state
            dfa.add_state(dfa_state)

            # Check if this new DFA state is an accepting state
            if nfa.accept_states & frozen:
                dfa.accept_states.add(dfa_state)
        return state_map[frozen]

    start_dfa_state = get_dfa_state({nfa.start_state})
    dfa.start_state = start_dfa_state

    unprocessed_states = [frozenset({nfa.start_state})]

    while unprocessed_states:
        current_nfa_states = unprocessed_states.pop()
        current_dfa_state = get_dfa_state(current_nfa_states)
        for symbol in nfa.alphabet:
            # Compute the union of NFA transitions for this symbol
            next_states = set(chain.from_iterable(
                nfa.transitions[state][symbol] for state in current_nfa_states
            ))
            if next_states:
                next_dfa_state = get_dfa_state(next_states)
                dfa.add_transition(current_dfa_state, symbol, next_dfa_state)
                if frozenset(next_states) not in state_map:
                    unprocessed_states.append(frozenset(next_states))

    return dfa


def print_dfa(dfa):
    print("States:", dfa.states)
    print("Start State:", dfa.start_state)
    print("Accept States:", dfa.accept_states)
    print("Transitions:")
    for (from_state, symbol), to_state in dfa.transitions.items():
        print(f"  {from_state} --{symbol}--> {to_state}")


# Example usage
nfa = NFA()
nfa.add_state("A", is_start=True)
nfa.add_state("B")
nfa.add_state("C", is_accept=True)
nfa.add_transition("A", "0", "A")
nfa.add_transition("A", "0", "B")
nfa.add_transition("B", "1", "C")

dfa = nfa_to_dfa(nfa)
print_dfa(dfa)
