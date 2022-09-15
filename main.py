from model.Automaton import Automaton

from init_data.data import automaton_uno


a1 = Automaton()
a2 = Automaton()

a1.load_automaton('init_data/automaton_one.json')
a2.load_automaton('init_data/automaton_two.json')

a2.print_event()
print()
a1.print_event()
