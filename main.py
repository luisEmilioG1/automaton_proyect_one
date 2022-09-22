from model.Automaton import Automaton
from controller.Automaton_operation import Operations

a1 = Automaton()
a2 = Automaton()

a1.load_automaton('init_data/automaton_one.json')
a2.load_automaton('init_data/automaton_two.json')

# a2.print_event()
# print()
# print('a2 ' + str(a2.is_incomplete()) + ' is complete')

a2.automaton_complement()
