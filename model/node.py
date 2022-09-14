class Node:

    def __init__(self, value: int, name: str):
        self._value = value
        self.name = name

    def get_value(self):
        return self._value
