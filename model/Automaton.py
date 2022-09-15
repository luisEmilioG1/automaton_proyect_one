from .State import State
from .Event import Event


class Automaton:
    def __init__(self, alphabet: list):
        self._event_list = []
        self._state_list = []
        self._initial_state = None
        self._alphabet = alphabet
        self._final_states = []

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

    def add_final_state(self, state_name: str):
        new_final_state = self._get_one_state(state_name)
        if not (new_final_state):
            raise Exception('el estado "'+state_name+'" no existe.')

        new_final_state.set_is_final(True)
        self._final_states.append(new_final_state)

    def add_state(self, name: str):
        node_exists = self._get_one_state(name)
        if (node_exists):
            raise Exception('el nodo "'+name+'" ya existe.')

        new_node = State(name)
        self._state_list.append(new_node)

    def add_event(self, init_node_name: str, final_node_name: str, names: list):
        init_node = self._get_one_state(init_node_name)
        final_node = self._get_one_state(final_node_name)

        if not (init_node) or not (final_node):
            raise Exception('alguno de los nodos no existe.')

        new_event = Event(init_node, final_node, names)
        self._event_list.append(new_event)

    def print_event(self):
        for event in self._event_list:
            init_node = event.get_init_state()
            final_node = event.get_final_state()
            names = event.get_names()

            print(init_node.get_name() + ' <-- ' +
                  str(names)+' --> '+final_node.get_name())