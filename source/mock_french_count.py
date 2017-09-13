from fst import FST
from fsmutils import composewords, trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.add_state('unit')
    f.add_state('tenth_0')
    f.add_state('tenth_1')
    f.add_state('tenth_2')
    f.add_state('tenth_3')
    f.add_state('tenth_4')
    f.add_state('tenth_5')
    f.add_state('tenth_6')
    f.add_state('tenth_7')
    f.add_state('tenth_8')
    f.add_state('tenth_9')
    f.add_state('hundred_0')
    f.add_state('hundred_1')
    f.add_state('hundred_2')
    f.add_state('hundred_3')
    f.add_state('hundred_4')
    f.add_state('hundred_5')
    f.add_state('hundred_6')
    f.add_state('hundred_7')
    f.add_state('hundred_8')
    f.add_state('hundred_9')

    f.initial_state = 'start'
    #f.set_final('start')
    f.set_final('unit')

    for num in xrange(10):
        # f.add_arc('start', 'start', [str(num)], [kFRENCH_TRANS[num]])
        if num == 0:
            # When 0 in hundredth place
            f.add_arc('start', 'hundred_0', [str(num)], [''])
            # When 0 in tenth place
            f.add_arc('hundred_0', 'tenth_0', [str(num)], [''])
            # When 1 in tenth and 0 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[10]])
            # When 2 in tenth and 0 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20]])
            # When 3 in tenth and 0 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [''])
            # When 4 in tenth and 0 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [''])
            # When 5 in tenth and 0 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [''])
            # When 6 in tenth and 0 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [''])
            # When 7 in tenth and 0 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10]])
            # When 8 in tenth and 0 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' '])
            # When 9 in tenth and 0 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10]])

        if num == 1:
            # When 0 in hundredth place and 1 in tenth place
            f.add_arc('hundred_0', 'tenth_1', [str(num)], [''])
            # When 1 in tenth and 1 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[11]])
            # When 2 in tenth and 1 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_AND + ' ' + kFRENCH_TRANS[1]])
            # When 3 in tenth and 1 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_AND + ' ' + kFRENCH_TRANS[1]])
            # When 4 in tenth and 1 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_AND + ' ' + kFRENCH_TRANS[1]])
            # When 5 in tenth and 1 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_AND + ' ' + kFRENCH_TRANS[1]])
            # When 6 in tenth and 1 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_AND + ' ' + kFRENCH_TRANS[1]])
            # When 7 in tenth and 1 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_AND + ' ' + kFRENCH_TRANS[11]])
            # When 8 in tenth and 1 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[1]])
            # When 9 in tenth and 1 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[11]])

        if num == 2:
            # When 0 in hundredth place and 2 in unit place
            f.add_arc('hundred_0', 'tenth_2', [str(num)], [''])
            # When 1 in tenth and 2 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[12]])
            # When 2 in tenth and 2 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[2]])
            # When 3 in tenth and 2 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[2]])
            # When 4 in tenth and 2 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[2]])
            # When 5 in tenth and 2 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[2]])
            # When 6 in tenth and 2 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[2]])
            # When 7 in tenth and 2 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[12]])
            # When 8 in tenth and 2 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[2]])
            # When 9 in tenth and 2 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[12]])
            pass

        if num == 3:
            # When 0 in hundredth place and 3 in unit place
            f.add_arc('hundred_0', 'tenth_3', [str(num)], [kFRENCH_TRANS[30]])
            # When 1 in tenth and 3 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[13]])
            # When 2 in tenth and 3 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[3]])
            # When 3 in tenth and 3 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[3]])
            # When 4 in tenth and 3 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[3]])
            # When 5 in tenth and 3 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[3]])
            # When 6 in tenth and 3 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[3]])
            # When 7 in tenth and 3 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[13]])
            # When 8 in tenth and 3 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[3]])
            # When 9 in tenth and 3 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[13]])
            pass

        if num == 4:
            # When 0 in hundredth place and 4 in unit place
            f.add_arc('hundred_0', 'tenth_4', [str(num)], [kFRENCH_TRANS[40]])
            # When 1 in tenth and 4 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[14]])
            # When 2 in tenth and 4 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[4]])
            # When 3 in tenth and 4 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[4]])
            # When 4 in tenth and 4 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[4]])
            # When 5 in tenth and 4 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[4]])
            # When 6 in tenth and 4 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[4]])
            # When 7 in tenth and 4 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[14]])
            # When 8 in tenth and 4 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[4]])
            # When 9 in tenth and 4 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[14]])
            pass

        if num == 5:
            # When 0 in hundredth place and 5 in unit place
            f.add_arc('hundred_0', 'tenth_5', [str(num)], [kFRENCH_TRANS[50]])
            # When 1 in tenth and 5 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[15]])
            # When 2 in tenth and 5 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[5]])
            # When 3 in tenth and 5 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[5]])
            # When 4 in tenth and 5 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[5]])
            # When 5 in tenth and 5 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[5]])
            # When 6 in tenth and 5 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[5]])
            # When 7 in tenth and 5 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[15]])
            # When 8 in tenth and 5 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[5]])
            # When 9 in tenth and 5 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[15]])
            pass

        if num == 6:
            # When 0 in hundredth place and 6 in unit place
            f.add_arc('hundred_0', 'tenth_6', [str(num)], [kFRENCH_TRANS[60]])
            # When 1 in tenth and 6 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[16]])
            # When 2 in tenth and 6 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[6]])
            # When 3 in tenth and 6 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[6]])
            # When 4 in tenth and 6 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[6]])
            # When 5 in tenth and 6 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[6]])
            # When 6 in tenth and 6 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[6]])
            # When 7 in tenth and 6 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[16]])
            # When 8 in tenth and 6 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[6]])
            # When 9 in tenth and 6 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[16]])
            pass

        if num == 7:
            # When 0 in hundredth place and 7 in unit place
            f.add_arc('hundred_0', 'tenth_7', [str(num)], [kFRENCH_TRANS[60]])
            # When 1 in tenth and 7 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[10]+' '+kFRENCH_TRANS[7]])
            # When 2 in tenth and 7 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[7]])
            # When 3 in tenth and 7 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[7]])
            # When 4 in tenth and 7 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[7]])
            # When 5 in tenth and 7 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[7]])
            # When 6 in tenth and 7 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[7]])
            # When 7 in tenth and 7 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10]+' '+kFRENCH_TRANS[7]])
            # When 8 in tenth and 7 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[7]])
            # When 9 in tenth and 7 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[7]])
            pass

        if num == 8:
            # When 0 in hundredth place and 8 in unit place
            f.add_arc('hundred_0', 'tenth_8', [str(num)], [kFRENCH_TRANS[4] + ' ' + kFRENCH_TRANS[20]])
            # When 1 in tenth and 8 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[8]])
            # When 2 in tenth and 8 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[8]])
            # When 3 in tenth and 8 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[8]])
            # When 4 in tenth and 8 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[8]])
            # When 5 in tenth and 8 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[8]])
            # When 6 in tenth and 8 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[8]])
            # When 7 in tenth and 8 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[8]])
            # When 8 in tenth and 8 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[8]])
            # When 9 in tenth and 8 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[8]])
            pass

        if num == 9:
            # When 0 in hundredth place and 9 in unit place
            f.add_arc('hundred_0', 'tenth_9', [str(num)], [kFRENCH_TRANS[4] + ' ' + kFRENCH_TRANS[20]])
            # When 1 in tenth and 9 in unit place
            f.add_arc('tenth_1', 'unit', [str(num)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[9]])
            # When 2 in tenth and 9 in unit place
            f.add_arc('tenth_2', 'unit', [str(num)], [kFRENCH_TRANS[20] + ' ' + kFRENCH_TRANS[9]])
            # When 3 in tenth and 9 in unit place
            f.add_arc('tenth_3', 'unit', [str(num)], [' ' + kFRENCH_TRANS[9]])
            # When 4 in tenth and 9 in unit place
            f.add_arc('tenth_4', 'unit', [str(num)], [' ' + kFRENCH_TRANS[9]])
            # When 5 in tenth and 9 in unit place
            f.add_arc('tenth_5', 'unit', [str(num)], [' ' + kFRENCH_TRANS[9]])
            # When 6 in tenth and 9 in unit place
            f.add_arc('tenth_6', 'unit', [str(num)], [' ' + kFRENCH_TRANS[9]])
            # When 7 in tenth and 9 in unit place
            f.add_arc('tenth_7', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[9]])
            # When 8 in tenth and 9 in unit place
            f.add_arc('tenth_8', 'unit', [str(num)], [' ' + kFRENCH_TRANS[9]])
            # When 9 in tenth and 9 in unit place
            f.add_arc('tenth_9', 'unit', [str(num)], [' ' + kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[9]])
            pass

        f.add_arc('tenth_0', 'unit', [str(num)], [kFRENCH_TRANS[num]])
# Larry, Chealsea - recruiter, Utkarsh SE

    return f

f = french_count()
print prepare_input(134)
n = 70
for n in range(0, 100):
    print "".join(f.transduce(prepare_input(n)))
print "".join(f.transduce(prepare_input(n)))
trace(f, prepare_input(n))
