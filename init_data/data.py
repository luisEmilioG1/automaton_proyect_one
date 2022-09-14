automaton_uno = {
    'X': ['Q1', 'Q2'],  # states
    'E': ['0', '1'],  # alphabet
    'X0': 'Q1',  # initial state
    'Xm': 'Q2',  # final states
    'fun_transition': [
        {'initial_state': 'Q1', 'event': '0', 'destination_state': 'Q2'},
        {'initial_state': 'Q1', 'event': '1', 'destination_state': 'Q1'},
        {'initial_state': 'Q2', 'event': '0', 'destination_state': 'Q2'}
    ]
}

automaton_two = {
    'X': ['Q1', 'Q2'],  # states
    'E': ['0', '1'],  # alphabet
    'X0': 'Q1',  # initial state
    'Xm': 'Q2',  # final states
    'fun_transition': [
        {'initial_state': 'Q1', 'event': '0', 'destination_state': 'Q2'},
        {'initial_state': 'Q1', 'event': '1', 'destination_state': 'Q1'},
        {'initial_state': 'Q2', 'event': '0', 'destination_state': 'Q2'}
    ]
}


