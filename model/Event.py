from .State import State


class Event:
    def __init__(self, init_state: State, final_state: State, names: list):
        self._init_state = init_state
        self._final_state = final_state
        self._names = names

    def get_init_state(self):
        return self._init_state

    def get_final_state(self):
        return self._final_state

    def get_names(self):
        return self._names
