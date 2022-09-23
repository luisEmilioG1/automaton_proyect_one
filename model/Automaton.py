from gettext import translation
from os import access
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

    def load_automaton_dict(self, automaton: dict):

        alphabet = automaton['alphabet']
        states = automaton['states']
        initial_state = automaton['initial_state']
        acceptance_states = automaton['acceptance_states']
        transitions = automaton['transitions']

        for state_name in states:
            self.add_state(state_name)

        for transition in transitions:
            origin_state = transition['source']
            destination_state = transition['destiny']
            event = transition['event']

            self.add_event(origin_state, destination_state, event)

        for state_name in acceptance_states:
            self.add_final_state(state_name)

        self.set_initial_state(initial_state)

        self.set_alphabet(alphabet)

        is_incomplete = self.is_incomplete()

        if not (is_incomplete):
            return

        # print('incompleto era...\n')
        # self.print_event()
        self.complete_automaton_sump(is_incomplete)
        # print('\nahora, completo es...\n')
        # self.print_event()

    def load_automaton(self, url: str):

        automaton = {}
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
            origin_state = transition['source']
            destination_state = transition['destiny']
            event = transition['event']

            self.add_event(origin_state, destination_state, event)

        for state_name in acceptance_states:
            self.add_final_state(state_name)

        self.set_initial_state(initial_state)

        self.set_alphabet(alphabet)

        is_incomplete = self.is_incomplete()

        if not (is_incomplete):
            return

        # print('incompleto era...\n')
        # self.print_event()
        self.complete_automaton_sump(is_incomplete)
        # print('\nahora, completo es...\n')
        # self.print_event()

    def get_state_list(self):
        return self._state_list

    def get_acceptance_states(self):
        return self._acceptance_states

    def set_acceptance_states(self, acceptance_states):
        self._acceptance_states = acceptance_states

    def _get_one_state(self, state_name):
        for node in self._state_list:
            if (state_name == node.get_name()):
                return node
        return None

    def _event_exists(self, event: Event):
        for self_event in self._event_list:
            self_init_state_name = self_event.get_init_state().get_name()
            self_final_state_name = self_event.get_final_state().get_name()
            self_names_event = self_event.get_names()

            init_state_name = event.get_init_state().get_name()
            final_state_name = event.get_final_state().get_name()
            names_event = event.get_names()

            if not (self_init_state_name == init_state_name and
                    self_final_state_name == final_state_name):
                return False

            for name in names_event:
                if (name in self_names_event):
                    return True

        return False

    def get_alphabet(self):
        return self._alphabet

    def set_alphabet(self, alphabet):
        self._alphabet = alphabet

    def get_initial_state(self):
        return self._initial_state

    def get_event_list(self):
        return self._event_list

    def set_initial_state(self, state_name: str):
        new_initial_state = self._get_one_state(state_name)
        if not (new_initial_state):
            raise Exception('el estado "'+state_name+'" no existe.')

        new_initial_state.set_is_initial(True)
        self._initial_state = new_initial_state

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

    def add_event(self, init_node_name: str, final_node_name: str, event: list):
        init_node = self._get_one_state(init_node_name)
        final_node = self._get_one_state(final_node_name)

        if not (init_node) or not (final_node):
            raise Exception(
                'intenta agregar una trancición a un estado que no existe.')

        new_event = Event(init_node, final_node, event)

        if (self._event_exists(new_event)):
            raise Exception('está repitiendo un orígen nombre y destino')

        self._event_list.append(new_event)

    def is_incomplete(self):
        transitions_of_initial_states = {}

        for event in self._event_list:
            init_node_name = event.get_init_state().get_name()
            event_names = event.get_names()

            for name in event_names:
                exist_initial_state = transitions_of_initial_states.get(
                    init_node_name, False)

                if not (exist_initial_state):
                    transitions_of_initial_states[init_node_name] = []
                    transitions_of_initial_states[init_node_name].append(name)
                    continue

                transitions_of_initial_states[init_node_name].append(name)

        missing_transitions = {}

        for initial_state in transitions_of_initial_states:
            missing_transition = list(
                set(self._alphabet) - set(transitions_of_initial_states[initial_state]))

            if (bool(missing_transition)):
                missing_transitions[initial_state] = missing_transition

        if (bool(missing_transitions)):
            return missing_transitions

        return False

    def complete_automaton_sump(self, missing_transitions: dict):
        self.add_state('sump')
        for init_state_name in missing_transitions:
            self.add_event(init_state_name, 'sump',
                           missing_transitions[init_state_name])
        self.add_event('sump', 'sump', self._alphabet)

    def print_event(self):
        for event in self._event_list:
            init_node_name = event.get_init_state()
            final_node = event.get_final_state()
            event_names = event.get_names()

            print(init_node_name.get_name() + ' -- ' +
                  str(event_names)+' --> '+final_node.get_name())

    def get_quintuple(self):
        states = []
        for state in self._state_list:
            states.append(state.get_name())

        alphabet = self._alphabet

        initial_state = self._initial_state.get_name()

        acceptance_states = []

        for acceptance in self._acceptance_states:
            acceptance_states.append(acceptance.get_name())

        transitions = []

        for transition in self._event_list:
            transitions.append({
                "source": transition.get_init_state().get_name(),
                "event": transition.get_names(),
                "destiny": transition.get_final_state().get_name()
            })

        return {
            "states": states,
            "alphabet": alphabet,
            "initial_state": initial_state,
            "acceptance_states": acceptance_states,
            "transitions": transitions
        }

    def automaton_complement(self):
        # print('Estado inicial', automaton_two._initial_state.get_name())

        normal_states = []

        for state in self.get_state_list():
            if state not in self.get_acceptance_states():
                normal_states.append(state.get_name())
        r = []
        for state in self.get_acceptance_states():
            r.append(state.get_name())
        print('Viejos estados de aceptacion', r)

        self.set_acceptance_states(normal_states)
        print('Nuevos estados de aceptacion', self.get_acceptance_states())
