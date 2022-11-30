from model.Automaton import Automaton
from controller.Convert_to_deterministic import ConvertToDeterministic
from controller.Automaton_operation import Operations

a1 = Automaton()
a2 = Automaton()
a3 = Automaton()
convert = ConvertToDeterministic(a3)

a3.load_automaton('init_data/converseToAFD.json')

convert.print_table()

afd = convert.converse()
convert.print_table()
print()
afd.print_event()
print(afd.get_quintuple())

