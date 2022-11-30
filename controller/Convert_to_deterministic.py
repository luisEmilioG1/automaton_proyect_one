from model.Event import Event
from model.State import State
from model.Automaton import Automaton


def concat_list(lst: [str]) -> str:
    lst = list(set(lst.copy()))  # remove duplicate
    concat = ''
    for e in lst:
        concat += ' ' + e

    return concat.rstrip().lstrip()


class ConvertToDeterministic:
    _table = []
    _automaton = None

    def __init__(self, automaton: Automaton):
        self._automaton = automaton

    def converse(self) -> Automaton:
        # header
        # self._table.append(['state', *self._automaton.get_alphabet()])
        self.complete_table()

        automatonFD = Automaton()

        automatonFD.set_alphabet(self._automaton.get_alphabet())
        transitions = []
        for row in self._table:
            # row[0] => column one
            init_state_name = row[0]
            automatonFD.add_state(init_state_name)
            for i in range(len(row) - 1):
                transitions.append({
                    'init_state': init_state_name,
                    'names': self._automaton.get_alphabet()[i],
                    'final_state': row[i + 1]
                })
        automatonFD.set_initial_state(self._table[0][0])

        # add events
        for event in transitions:
            if not event['final_state']:
                continue
            automatonFD.add_event(event['init_state'], event['final_state'], [event['names']])

        # setter acceptances states
        acceptances = list(map(lambda x: x.get_name(), self._automaton.get_acceptance_states()))
        for state in automatonFD.get_state_list():
            for acceptance in acceptances:
                if acceptance in state.get_name():
                    automatonFD.add_final_state(state.get_name())

        return automatonFD

    def complete_table(self, table=None):
        if not table:
            # first row
            initial_state = self._automaton.get_initial_state()
            destines = self.destines_state(initial_state.get_name())

            self._table.append([initial_state.get_name(), *destines])
            self.complete_table(self._table)
            return

        for row in table:
            # row[0] = state name
            for row_position in range(len(self._automaton.get_alphabet())):
                # events with composer name -> A B D
                event_name = row[row_position + 1]

                if self.table_use_event_name(event_name) or not event_name:
                    continue

                event_simple_name = event_name.split(' ')
                destines = self.destines_multiple_states(*event_simple_name)
                self._table.append([event_name, *destines])
                self.complete_table(self._table)
                return

    def table_use_event_name(self, event_name: str) -> bool:
        for row in self._table:
            if event_name == row[0]:
                return True

        return False

    def destines_state(self, state_name: str) -> [str]:
        destines = []
        for alphabet_character in self._automaton.get_alphabet():
            destines.append(self.destines_with_alphabet_character_lamda(state_name, alphabet_character))
        return destines

    def destines_multiple_states(self, *states_name: [str]) -> [str]:
        destines = []

        for alphabet_character in self._automaton.get_alphabet():

            destines_one_alphabet_character = ''
            for state_name in states_name:

                # full_destines = self.destines_with_alphabet_character(state_name, alphabet_character)
                full_destines = self.destines_with_alphabet_character_lamda(state_name, alphabet_character)
                if full_destines in destines_one_alphabet_character:
                    continue
                if len(destines_one_alphabet_character) == 0:
                    destines_one_alphabet_character += full_destines
                    continue

                destines_one_alphabet_character += ' ' + full_destines
            destines_order_list = destines_one_alphabet_character.split(' ')
            destines_order_list.sort()

            destines.append(concat_list(destines_order_list))

        return destines

    # no use
    def destines_with_alphabet_character(self, state_name: str, alphabet_character: str) -> str:
        destine = ''
        for event in self._automaton.get_event_list():
            if state_name == event.get_init_state().get_name() and alphabet_character in event.get_names():
                if len(destine) == 0:
                    destine = event.get_final_state().get_name()
                    continue

                destine += ' ' + event.get_final_state().get_name()
        destine_order_list = destine.split(' ')
        destine_order_list.sort()

        return concat_list(destine_order_list)

    def destines_with_alphabet_character_lamda(self, state_name: str, alphabet_character: str) -> str:
        initial_events = []
        destines = []
        for event in self._automaton.get_event_list():
            if event.get_init_state().get_name() == state_name:
                initial_events.append(event)

        for initial_event in initial_events:
            self.visit_events_with_lamda(initial_event, state_name, alphabet_character, destines)

        return concat_list(destines)

    def visit_events_with_lamda(self, actual_event: Event, state_name: str, alphabet_character: str,
                                destines_lamda: [str], counter_alphabet_character=0):
        if alphabet_character not in actual_event.get_names() and 'λ' not in actual_event.get_names():
            return

        if alphabet_character in actual_event.get_names():
            counter_alphabet_character += 1

        if counter_alphabet_character == 1:
            # print(actual_event.get_final_state().get_name())
            destines_lamda.append(actual_event.get_final_state().get_name())

        if counter_alphabet_character > 1:
            return

        for event in self._automaton.get_event_list():
            if event.get_init_state() == actual_event.get_final_state():
                self.visit_events_with_lamda(event, state_name, alphabet_character, destines_lamda,
                                             counter_alphabet_character)

    def print_table(self):
        for row in self._table:
            print(row)
