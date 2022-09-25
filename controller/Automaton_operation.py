from model.Automaton import Automaton


class Operations:

    @staticmethod
    def automaton_union(automaton_one: Automaton, automaton_two: Automaton):
        states_automaton_one = automaton_one.get_state_list()
        states_automaton_two = automaton_two.get_state_list()

        new_states = []
        new_alphabet = automaton_one.get_alphabet()
        new_acceptance_states = []
        new_initial_state = None
        for state_one in states_automaton_one:
            for state_two in states_automaton_two:
                new_state = state_one.get_name()+state_two.get_name()
                new_states.append(new_state)

                if (state_one in automaton_one.get_acceptance_states() or state_two in automaton_two.get_acceptance_states()):
                    new_acceptance_states.append(new_state)

                if (state_one == automaton_one.get_initial_state() and state_two == automaton_two.get_initial_state()):
                    new_initial_state = new_state

        new_transitions = []
        for transition_one in automaton_one.get_event_list():
            name_state_origin_transitio_one = transition_one.get_init_state().get_name()
            name_state_dstiny_transitio_one = transition_one.get_final_state().get_name()

            for transition_two in automaton_two.get_event_list():
                name_state_origin_transitio_two = transition_two.get_init_state().get_name()
                name_state_destiny_transitio_two = transition_two.get_final_state().get_name()

                for name_transition_one in transition_one.get_names():
                    for name_transition_two in transition_two.get_names():
                        if (name_transition_one == name_transition_two):
                            """  print(name_state_origin_transitio_one+" con " +
                                name_transition_one+" va a "+name_state_dstiny_transitio_one)
                            print("yyyyy")
                            print(name_state_origin_transitio_two+" con " +
                                name_transition_one+" va a "+name_state_destiny_transitio_two)
                            print("entonces, "+name_state_origin_transitio_one+name_state_origin_transitio_two+" con " +
                                name_transition_one + " va a "+name_state_dstiny_transitio_one+name_state_destiny_transitio_two)
                            print() """

                            origin = name_state_origin_transitio_one+name_state_origin_transitio_two
                            destiny = name_state_dstiny_transitio_one+name_state_destiny_transitio_two

                            new_transitions.append(
                                {"source": origin, "event": [name_transition_one], "destiny": destiny})

        quintuple_automaton_unio = {
            "states": new_states,
            "alphabet": new_alphabet,
            "initial_state": new_initial_state,
            "acceptance_states": new_acceptance_states,
            "transitions": new_transitions
        }

        automaton_unio = Automaton()
        automaton_unio.load_automaton_dict(quintuple_automaton_unio)
        # automaton_unio.print_event()
        return automaton_unio

        #print("los nuevos estados son: ", new_states)
        #print("los nuevos estados de aceptación: ", new_acceptance_states)
        #print("el nuevos estado inicial es: ", new_initial_state)
        #print("las nuevas transiciones son: ", new_transitions)

    @staticmethod
    def automaton_complement(automaton: Automaton):
        normal_states = []
        for state in automaton.get_state_list():
            if state not in automaton.get_acceptance_states():
                normal_states.append(state)
        r = []
        for state in automaton.get_acceptance_states():
            r.append(state)

        automaton.set_acceptance_states(normal_states)

        return automaton

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
        # print(sinks)
        automaton.print_event()
        return automaton

    def create_new_acceptance(automaton):
        automaton.add_state('lamb')
        for state in automaton.get_acceptance_states():
            automaton.add_event(state.get_name(), 'lamb', ['lambda'])
        automaton.set_acceptance_states([automaton._get_one_state('lamb')])
        print('_________________')
        print('El nuevo estado de acceptacion es:',
            automaton.get_acceptance_states()[0].get_name())
