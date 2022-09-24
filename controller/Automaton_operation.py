from model.Automaton import Automaton


class Operations:

    @staticmethod
    def automaton_reverse(automaton: Automaton):

        if len(automaton.get_acceptance_states()) > 1:
            automaton.create_new_acceptance()

        automaton.print_event()

        print('----------------')

        for event in automaton._event_list:
            init_node_name = event.get_final_state()
            final_node = event.get_init_state()
            event_names = event.get_names()

            event.set_init_state(init_node_name)
            event.set_final_state(final_node)

            print(init_node_name.get_name() + ' -- ' +
                  str(event_names)+' --> '+final_node.get_name())

        acceptance_state = automaton.get_initial_state()
        automaton._initial_state = automaton.get_acceptance_states()[0]
        automaton.set_acceptance_states([acceptance_state])

        print('Estado Inicial ', acceptance_state.get_name())
        print('Nuevo estado inicial ', automaton.get_initial_state().get_name())
        print('Estado Final antes ', automaton._initial_state.get_name())
        print('Nuevo estado final ',
              automaton.get_acceptance_states()[0].get_name())

        origin_states = []
        attainable_states = []
        for event in automaton._event_list:
            if event.get_init_state().get_name() != event.get_final_state().get_name():
                """print(event.get_init_state().get_name(),
                      event.get_final_state().get_name())"""
                if event.get_init_state() not in origin_states:
                    origin_states.append(event.get_init_state())
                if event.get_final_state() not in attainable_states:
                    attainable_states.append(event.get_final_state())
            """print(event.get_init_state().get_name(),
                  event.get_final_state().get_name(), "-----------")"""

        """r = []
        for state in origin_states:
            r.append(state.get_name())
        print(r)
        r2 = []
        for state in attainable_states:
            r2.append(state.get_name())
        print(r2)"""

        sinks = []
        for event in automaton._event_list:
            """print(event.get_init_state().get_name(),
                  event.get_final_state().get_name(), "-----------")"""
            for state in origin_states:
                if event.get_init_state().get_name() == state.get_name() or event.get_final_state().get_name() == state.get_name():
                    if (state not in attainable_states) and (state != automaton.get_initial_state()):
                        automaton._event_list.remove(event)
                        if event.get_init_state() not in sinks:
                            sinks.append(event.get_init_state())

        for sink in sinks:
            for event in automaton._event_list:
                if event.get_init_state().get_name() == sink.get_name() or event.get_final_state().get_name() == sink.get_name():
                    automaton._event_list.remove(event)

        #print(sinks)

        automaton.print_event()

    def create_new_acceptance(automaton):
        automaton.add_state('lamb')
        for state in automaton.get_acceptance_states():
            automaton.add_event(state.get_name(), 'lamb', ['lambda'])
        automaton.set_acceptance_states([automaton._get_one_state('lamb')])
        print('_________________')
        print('El nuevo estado de acceptacion es:',
              automaton.get_acceptance_states()[0].get_name())
