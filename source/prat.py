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
    
    f1.add_state('replace1')
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

    # Add the rest of the arcs
    for letter in string.ascii_lowercase:
        # print letter
        f1.add_arc('start', 'next', (letter), (letter))
        if letter in remove:
            f1.add_arc('next', 'next', (letter), (''))

        if letter in replace_1:
            f1.add_arc('next', 'next', (letter), ('1'))
        #     f1.add_arc('next', 'replace1', (letter), ('1'))
        #     f1.add_arc('replace1', 'replace1', (letter), (''))
        # else:
        #     f1.add_arc('replace1', 'next', (), ())

        if letter in replace_2:
            f1.add_arc('next', 'next', (letter), ('2'))
        if letter in replace_3:
            f1.add_arc('next', 'next', (letter), ('3'))
        if letter in replace_4:
            f1.add_arc('next', 'next', (letter), ('4'))
        if letter in replace_5:
            f1.add_arc('next', 'next', (letter), ('5'))
        if letter in replace_6:
            f1.add_arc('next', 'next', (letter), ('6'))

        # else:
        #     f1.add_arc('next', 'next', (letter),('9'))

        # elif letter in replace_1:
        #     f1.add_arc('next', 'next', (letter), ('1'))
        # else:
        #     f1.add_arc('start', 'next', (letter), (letter))
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?


def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2_N')
    f2.add_state('2_L')
    f2.add_state('3')
    f2.add_state('4')

    f2.initial_state = '1'
    f2.set_final('4')
    f2.set_final('2_N')
    f2.set_final('2_L') # Check whether you want to keep this condition
    f2.set_final('3')
    f2.set_final('4')


    # Add the arcs
    for letter in string.letters:
        # f2.add_arc('1', '1', (letter), (letter))
        f2.add_arc('1', '2_L', (letter), (letter))
        f2.add_arc('2_L', '2_L', (letter), (''))

        for number in range(10):
            f2.add_arc('2_L', '2_N', (str(number)),(str(number)))


    for n in range(10):
        f2.add_arc('1', '2_N', (str(n)), (str(n)))
        f2.add_arc('2_N', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))
        f2.add_arc('4', '4', (str(n)), (''))

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?


def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2_N')
    f3.add_state('2_L')
    f3.add_state('3')
    f3.add_state('4')

    f3.initial_state = '1'
    f3.set_final('4')

    for letter in string.letters:
        f3.add_arc('1', '2_L', (letter), (letter))
        f3.add_arc('2_L', '2_L', (letter), (''))
        f3.add_arc('2_L', '2_N', (), ('0'))
        for number in range(10):
            f3.add_arc('2_L', '2_N', (str(number)), (str(number)))

    f3.add_arc('2_N', '3', (), ('0'))
    f3.add_arc('3', '4', (), ('0'))

    for number in xrange(10):
        f3.add_arc('1', '2_N', (str(number)), (str(number)))
        f3.add_arc('2_N', '3', (str(number)), (str(number)))
        f3.add_arc('3', '4', (str(number)), (str(number)))
        #f3.add_arc('4', '4', (str(number)), (''))

    #f3.add_arc('1', '2_N', (), ('0'))
    #f3.add_arc('2_L', '3', (), ('0'))
    # f3.add_arc('2_N', '3', (), ('0'))
    # f3.add_arc('3', '4', (), ('0'))
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!


f1 = letters_to_numbers()
f2 = truncate_to_three_digits()
f3 = add_zero_padding()

s = ['j', 'u', 'e', 'r', 't', 'y', 'b']
p = ['j', 'u', 'r', 'a', 'f', 's', 'k', 'y']
# trace(f1, p)
# print(composechars(p, f1))
# print "".join(f1.transduce(x for x in 'jeffersontthhggddzz'))
# trace(f1, (x for x in 'jeffersontthhggdd'))

# print "".join(f2.transduce(x for x in 'j'))
# trace(f2,(x for x in '1'))

# q = 'j'
# print "".join(f3.transduce(x for x in q))
# trace(f3, (x for x in q))