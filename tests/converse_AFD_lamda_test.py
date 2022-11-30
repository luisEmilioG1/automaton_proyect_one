from controller.Convert_to_deterministic import ConvertToDeterministic
from model.Automaton import Automaton


def converse_one_test():
    automaton_url = '../init_data_afd/converseToAFD.json'

    automaton = Automaton()
    automaton.load_automaton(automaton_url)
    converse = ConvertToDeterministic(automaton)

    # destines = converse.destines_with_alphabet_character_lamda('S', 'a')
    # print(destines)

    afd = converse.converse()

    afd.print_event()
    print(afd.get_quintuple())


def converse_two_test():
    automaton_url = '../init_data_afd/converseToAFDTwo.json'

    automaton = Automaton()
    automaton.load_automaton(automaton_url)
    converse = ConvertToDeterministic(automaton)

    # destines = converse.destines_with_alphabet_character_lamda('S', 'a')
    # print(destines)

    afd = converse.converse()

    afd.print_event()
    print(afd.get_quintuple())


def converse_lamda_one_test():
    automaton_url = '../init_data_afd/converseToAFDLamda.json'

    automaton = Automaton()
    automaton.load_automaton(automaton_url)
    converse = ConvertToDeterministic(automaton)

    # destines = converse.destines_with_alphabet_character_lamda('S', 'a')
    # print(destines)

    afd = converse.converse()

    afd.print_event()
    print(afd.get_quintuple())


def converse_lamda_two_test():
    automaton_url = '../init_data_afd/converseToAFDLamdaTwo.json'

    automaton = Automaton()
    automaton.load_automaton(automaton_url)
    converse = ConvertToDeterministic(automaton)

    # destines = converse.destines_with_alphabet_character_lamda('S', 'a')
    # print(destines)

    afd = converse.converse()

    afd.print_event()
    print(afd.get_quintuple())


def converse_lamda_three_test():
    automaton_url = '../init_data_afd/converseToAFDLamdaThree.json'

    automaton = Automaton()
    automaton.load_automaton(automaton_url)
    converse = ConvertToDeterministic(automaton)

    # destines = converse.destines_with_alphabet_character_lamda('S', 'a')
    # print(destines)

    afd = converse.converse()

    afd.print_event()
    print(afd.get_quintuple())

# converse_one_test()
converse_two_test()


# converse_lamda_one_test()
# converse_lamda_two_test()
# converse_lamda_three_test()