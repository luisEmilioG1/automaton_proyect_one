class State:

    def __init__(self, name: str):
        self._name = name
        self._is_initial = False
        self._is_final = False

    def get_name(self):
        return self._name

    def set_is_initial(self, is_initial: bool):
        self._is_initial = is_initial

    def set_is_final(self, is_final: bool):
        self._is_final = is_final

    def get_is_initial(self):
        return self._is_initial

    def get_is_final(self):
        return self._is_final
