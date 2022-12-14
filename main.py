from model.Automaton import Automaton
from controller.Automaton_operation import Operations

a1 = Automaton()
a2 = Automaton()
a3 = Automaton()

#a1.load_automaton('init_data/automaton_one.json')
#a2.load_automaton('init_data/automaton_two.json')

a3.load_automaton('init_data/automaton_three.json')

# a2.print_event()
# print()
# print('a2 ' + str(a2.is_incomplete()) + ' is complete')

Operations.automaton_complement(a3)

print(a3.switch_to_notation())
Operations.automaton_reverse(a3)

print(a3.switch_to_notation())

"""Operations.automaton_reverse(a3)

a1.load_automaton('init_data/for_unio_one.json')
a2.load_automaton('init_data/for_unio_two.json')
# a2.automaton_complement()

Operations.automaton_union(a1, a2)"""
