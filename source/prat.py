from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next')

    remove = ['a', 'e', 'h', 'i', 'o', 'u', 'w', 'y']
    replace_1 = ['b', 'f', 'p', 'v']
    replace_2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']
    replace_3 = ['d', 't']
    replace_4 = ['l']
    replace_5 = ['m', 'n']
    replace_6 = ['r']
    last_group = 0
    # Add the rest of the arcs
    for letter in string.ascii_lowercase:
        f1.add_arc('start', 'next', (letter), (letter))
        if letter in remove:
            f1.add_arc('next', 'next', (letter), (''))
        elif letter in replace_1:
            f1.add_arc('next', 'next', (letter), ('1'))
            last_group = 1
        elif letter in replace_2:
            f1.add_arc('next', 'next', (letter), ('2'))
            last_group = 2
        elif letter in replace_3:
            f1.add_arc('next', 'next', (letter), ('3'))
            last_group = 3
        elif letter in replace_4:
            f1.add_arc('next', 'next', (letter), ('4'))
            last_group = 4
        elif letter in replace_5:
            f1.add_arc('next', 'next', (letter), ('5'))
            last_group = 5
        elif letter in replace_6:
            f1.add_arc('next', 'next', (letter), ('6'))
            last_group = 6
        else:
            f1.add_arc('next', 'next', (letter),('9'))
        # elif letter in replace_1:
        #     f1.add_arc('next', 'next', (letter), ('1'))
        # else:
        #     f1.add_arc('start', 'next', (letter), (letter))
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

f = letters_to_numbers()
s = ['j', 'u', 'e', 'r', 't', 'y', 'b']
p = ['j', 'u', 'r', 'a', 'f', 's', 'k', 'y']
trace(f, p)
print(composechars(p, f))
print "".join(f.transduce(x for x in 'jefferson'))
