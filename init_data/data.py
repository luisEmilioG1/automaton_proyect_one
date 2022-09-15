automaton_uno = {
    'X': ['Q1', 'Q2'],  # states
    'E': ['0', '1'],  # alphabet
    'X0': 'Q1',  # initial state
    'Xm': ['Q2', 'Q1'],  # final states
    'fun_transition': [
        {'initial_state': 'Q1', 'names': ['0'], 'destination_state': 'Q2'},
        {'initial_state': 'Q1', 'names': ['1'], 'destination_state': 'Q1'},
        {'initial_state': 'Q2', 'names': ['0', '1'], 'destination_state': 'Q1'},
    ]
}

automaton_two = {
    'X': ['Q1', 'Q2'],  # states
    'E': ['0', '1'],  # alphabet
    'X0': 'Q1',  # initial state
    'Xm': ['Q2'],  # final states
    'fun_transition': [
        {'initial_state': 'Q1', 'names': ['0'], 'destination_state': 'Q2'},
        {'initial_state': 'Q1', 'names': ['1'], 'destination_state': 'Q1'},
        {'initial_state': 'Q2', 'names': ['0'], 'destination_state': 'Q2'}
    ]
}
