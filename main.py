from model.Automaton import Automaton

from init_data.data import automaton_uno

alphabet = automaton_uno['E']
states = automaton_uno['X']
initial_state = automaton_uno['X0']
final_states = automaton_uno['Xm']
functions_transition = automaton_uno['fun_transition']

automaton1 = Automaton(alphabet)

for state_name in states:
    automaton1.add_state(state_name)

for transition in functions_transition:
    initial_state = transition['initial_state']
    destination_state = transition['destination_state']
    names = transition['names']

    automaton1.add_event(initial_state, destination_state, names)

for state_name in final_states:
    automaton1.add_final_state(state_name)

automaton1.set_initial_state(initial_state)

automaton1.print_event()
