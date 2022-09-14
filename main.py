from model import State
from model import Automaton
from controller.automaton_operation import Operations
from init_data.data import automaton_uno

node_one = State(12, "Luis")
automaton_one = Automaton()
automaton_two = Automaton()

print(automaton_uno['fun_transition'][1]['event'])
