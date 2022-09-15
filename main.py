from model.State import State
from model.Automaton import Automaton
from model.Event import Event

from init_data.data import automaton_uno

e1 = State('E1')
e2 = State('E2')

t1 = Event(e1, e1, ['1'])
t2 = Event(e1, e2, ['0'])
t3 = Event(e2, e1, ['0', '1'])

automaton1 = Automaton(['0', '1'])
automaton1.add_state('E1')
automaton1.add_state('E2')

automaton1.add_event('E1', 'E1', ['1'])
automaton1.add_event('E1', 'E2', ['0'])
automaton1.add_event('E2', 'E1', ['0', '1'])

automaton1.set_initial_state('E1')
automaton1.add_final_state('E2')

automaton1.print_event()
