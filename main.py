
import json
from model.Automaton import Automaton
from controller.Automaton_operation import Operations

a1 = Automaton()
a2 = Automaton()

a1.load_automaton('init_data/for_unio_one.json')
a2.load_automaton('init_data/for_unio_two.json')
# a2.automaton_complement()

Operations.automaton_union(a1, a2)
