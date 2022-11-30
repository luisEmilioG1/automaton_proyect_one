from controller.Convert_to_deterministic import ConvertToDeterministic
from model.Automaton import Automaton

print('hello')

AUTOMATON_URL = 'init_data/converseToAFDLamdaTwo.json'

automaton = Automaton()
automaton.load_automaton(AUTOMATON_URL)

converse = ConvertToDeterministic(automaton)

destines = converse.destines_with_alphabet_character_lamda('0', 'a')

print(destines)