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
                            """ print(name_state_origin_transitio_one+" con " +
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
