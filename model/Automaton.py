from .State import State
from .Event import Event

import json


class Automaton:
    def __init__(self):
        self._event_list = []
        self._state_list = []
        self._alphabet = []
        self._initial_state = None
        self._acceptance_states = []

    def load_automaton(self, url: str):

        automaton = ''
        with open(url) as content:
            automaton = json.load(content)

        alphabet = automaton['alphabet']
        states = automaton['states']
        initial_state = automaton['initial_state']
        acceptance_states = automaton['acceptance_states']
        transitions = automaton['transitions']

        for state_name in states:
            self.add_state(state_name)

        for transition in transitions:
            initial_state = transition['source']
            destination_state = transition['destiny']
            event = transition['event']

            self.add_event(initial_state, destination_state, event)

        for state_name in acceptance_states:
            self.add_final_state(state_name)

        self.set_initial_state(initial_state)

        self.set_alphabet(alphabet)

    def _get_one_state(self, state_name):
        for node in self._state_list:
            if (state_name == node.get_name()):
                return node
        return None

    def set_initial_state(self, state_name: str):
        new_initial_state = self._get_one_state(state_name)
        if not (new_initial_state):
            raise Exception('el estado "'+state_name+'" no existe.')

        new_initial_state.set_is_initial(True)
        self._initial_state = new_initial_state

    def set_alphabet(self, alphabet: str):
        self._alphabet = alphabet

    def add_final_state(self, state_name: str):
        new_final_state = self._get_one_state(state_name)
        if not (new_final_state):
            raise Exception('el estado "'+state_name+'" no existe.')

        new_final_state.set_is_final(True)
        self._acceptance_states.append(new_final_state)

    def add_state(self, name: str):
        node_exists = self._get_one_state(name)
        if (node_exists):
            raise Exception('el nodo "'+name+'" ya existe.')

        new_node = State(name)
        self._state_list.append(new_node)

    def _event_exists(self, event: Event):
        for self_event in self._event_list:
            self_init_state_name = self_event.get_init_state().get_name()
            self_final_state_name = self_event.get_final_state().get_name()

            init_state_name = event.get_init_state().get_name()
            final_state_name = event.get_final_state().get_name()

            if (self_init_state_name == init_state_name and
                    self_final_state_name == final_state_name):
                return True

        return False

    def add_event(self, init_node_name: str, final_node_name: str, event: list):
        init_node = self._get_one_state(init_node_name)
        final_node = self._get_one_state(final_node_name)

        if not (init_node) or not (final_node):
            raise Exception('alguno de los estados no existe.')

        new_event = Event(init_node, final_node, event)

        if (self._event_exists(new_event)):
            raise Exception('el evento ya existe.')

        self._event_list.append(new_event)

    def print_event(self):
        for event in self._event_list:
            init_node = event.get_init_state()
            final_node = event.get_final_state()
            event = event.get_names()

            print(init_node.get_name() + ' -- ' +
                  str(event)+' --> '+final_node.get_name())
