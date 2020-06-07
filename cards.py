import random

# def card_number(number):
#     if number = 14:
#         aces += 1
#     if number = 2:
#         twos += 1
#     if number = 3:
#         threes += 1
#     if number = 4:
#         fours += 1
#     if number = 5:
#         fives += 1
#     if number = 6:
#         sixes += 1
#     if number = 7:
#         sevens += 1
#     if number = 8:
#         eights += 1
#     if number = 9:
#         nines += 1
#     if number = 10:
#         tens += 1
#     if number = 11:
#         jacks += 1
#     if number = 12:
#         queens += 1
#     if number = 13:
#         kings += 1
#     return aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings

tot_fullhouse = 0
tot_fourofakind = 0
tot_threeofakind = 0
tot_twopair = 0
tot_onepair = 0
for v in range(15000):

    aces = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    jacks = 0
    queens = 0
    kings = 0



    dealthand  = []
    numcheckhand = []
    while len(dealthand) < 5:
        number = random.randrange(1,14)
        card = random.randrange(1, 4)
        if number == 1:
            #aces += 1
            numberprint = 'A'
        elif number == 2:
            #twos += 1
            numberprint = '2'
        elif number == 3:
            #threes += 1
            numberprint = '3'
        elif number == 4:
            #fours += 1
            numberprint = '4'
        elif number ==5:
            #fives += 1
            numberprint = '5'
        elif number == 6:
            #sixes += 1
            numberprint = '6'
        elif number == 7:
            #sevens += 1
            numberprint = '7'
        elif number == 8:
            #eights += 1
            numberprint = '8'
        elif number == 9:
            #nines += 1
            numberprint = '9'
        elif number == 10:
            #tens += 1
            numberprint = '10'
        elif number == 11:
            #jacks += 1
            numberprint = 'J'
        elif number == 12:
            #queens += 1
            numberprint = 'Q'
        elif number == 13:
            #kings += 1
            numberprint = 'K'
        else:
            continue


        if card ==1:
            cardprint = '\u2663'
        elif card == 2:
            cardprint = '\u2666'
        elif card == 3:
            cardprint = '\u2665'
        else:
            cardprint = '\u2664'

        cardinhand = ( numberprint + cardprint)
        if cardinhand in dealthand:
            continue
        else:
            dealthand.append(cardinhand)
            numcheckhand.append(numberprint)
    #cardnum =[aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings]
    for item in numcheckhand:
        if item == 'A':
            aces += 1
        elif item == '2':
            twos += 1
        elif item == '3':
            threes += 1
        elif item == '4':
            fours += 1
        elif item == '5':
            fives += 1
        elif item == '6':
            sixes += 1
        elif item == '7':
            sevens += 1
        elif item == '8':
            eights += 1
        elif item == '9':
            nines += 1
        elif item == '10':
            tens += 1
        elif item == 'J':
            jacks += 1
        elif item == 'Q':
            queens += 1
        elif item == 'K':
            kings += 1
    cardnum = [aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings]



    four_of_a_kind = 0
    three_of_a_kind = 0
    two_pair = 0
    full_house = 0
    pair = 0


    if 4 in cardnum:
        four_of_a_kind +=1
    if 3 in cardnum:
        three_of_a_kind +=1
    if 2 in cardnum:
        pair += 1

    if three_of_a_kind == 1 and pair == 1:
        full_house += 1
        tot_fullhouse += 1
        #print('full house')
    elif three_of_a_kind == 1 and pair == 0:
        #print('three of a kind')
        three_of_a_kind += 1
        tot_threeofakind += 1
    elif four_of_a_kind == 1:
        #print('four of a kind')
        four_of_a_kind += 1
        tot_fourofakind += 1
    elif pair == 2:
        #print('two pair')
        two_pair += 1
        tot_twopair += 1
    elif pair == 1:
        #print('pair')
        pair += 1
        tot_onepair += 1
    #else:
        #print('rainbow')

    # print('4 of a kind')
    # print('3 of a kind')
    #print(dealthand)
    #print(numcheckhand)
    #print(cardnum)
    #cardnum = []

print('four of a kind {}'.format(tot_fourofakind))
print('fullhouse {}'.format(tot_fullhouse))
print('three of a kind {}'.format(tot_threeofakind))
print('two pair {}'.format(tot_twopair))
print('pair = {}'.format(tot_onepair))




# print ('aces = {}, twos = {}, threes = {}, fours = {}, fives = {}, sixes = {}, sevens = {}, eights = {}, nines = {}, tens = {}, jacks = {}, queens = {}, kings = {}, others = {}'.format(aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings, others))




