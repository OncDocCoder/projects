import random

def suit_up(suit):
    if suit ==0:
        cs = '\u2665'
        #cs = '\033[1;35;20m blue'
    elif suit == 1:
        cs = '\u2666'
    elif suit ==2:
        cs = '\u2663'
    else:
        cs = '\u2660'
    return cs

def card_name(c):
    if c == 0:
        card_val= 'A'
    elif c == 1:
        card_val= 'K'
    elif c == 2:
        card_val= 'Q'
    elif c == 3:
        card_val= 'J'
    elif c == 4:
        card_val= '10'
    elif c == 5:
        card_val= '9'
    elif c == 6:
        card_val= '8'
    elif c == 7:
        card_val= '7'
    elif c == 8:
        card_val= '6'
    elif c == 9:
        card_val = '5'
    elif c == 10:
        card_val = '4'
    elif c == 11:
        card_val = '3'
    else:
        card_val = '2'
    return card_val

def check_for_pairsplus(numbers):
    a = 0
    b= 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    for x in numbers:
        if x == 'A':
            a += 1
        if x == "2":
            b += 1
        if x == '3':
            c += 1
        if x == "4":
            d += 1
        if x == '5':
            e += 1
        if x == "6":
            f += 1
        if x == '7':
            g += 1
        if x == "8":
            h += 1
        if x == '9':
            i += 1
        if x == "10":
            j += 1
        if x == 'J':
            k += 1
        if x == "Q":
            l += 1
        if x == 'K':
            m += 1
    numskull = []
    numskull.extend((a, b, c, d, e, f, g, h, i, j, k, l, m) )
    return numskull

def the_num_of_multiples(seven, a):
    b= seven.index(a)

    if b == 0:
        card_val = 'A'
    elif b == 12:
        card_val = 'K'
    elif b == 11:
        card_val = 'Q'
    elif b == 10:
        card_val = 'J'
    elif b == 9:
        card_val = '10'
    elif b == 8:
        card_val = '9'
    elif b == 7:
        card_val = '8'
    elif b == 6:
        card_val = '7'
    elif b == 5:
        card_val = '6'
    elif b == 4:
        card_val = '5'
    elif b == 3:
        card_val = '4'
    elif b == 2:
        card_val = '3'
    else:
        card_val = '2'
    return card_val

def where_are_the_pairs(seven):

    c = [i for i, e in enumerate(seven) if e == 2]
    if c[0] == 0:
        card_val = 'A'
    elif c[0] == 12:
        card_val = 'K'
    elif c[0] == 11:
        card_val = 'Q'
    elif c[0] == 10:
        card_val = 'J'
    elif c[0] == 9:
        card_val = '10'
    elif c[0] == 8:
        card_val = '9'
    elif c[0] == 7:
        card_val = '8'
    elif c[0] == 6:
        card_val = '7'
    elif c[0] == 5:
        card_val = '6'
    elif c[0] == 4:
        card_val = '5'
    elif c[0] == 3:
        card_val = '4'
    elif c[0] == 2:
        card_val = '3'
    elif c[0] == 1:
        card_val = '2'
    if c[1] == 0:
        card_valb = 'A'
    elif c[1] == 12:
        card_valb = 'K'
    elif c[1] == 11:
        card_valb = 'Q'
    elif c[1] == 10:
        card_valb = 'J'
    elif c[1] == 9:
        card_valb = '10'
    elif c[1] == 8:
        card_valb = '9'
    elif c[1] == 7:
        card_valb = '8'
    elif c[1] == 6:
        card_valb = '7'
    elif c[1] == 5:
        card_valb = '6'
    elif c[1] == 4:
        card_valb = '5'
    elif c[1] == 3:
        card_valb = '4'
    elif c[1] == 2:
        card_valb = '3'
    elif c[1] == 1:
        card_valb = '2'
    return  card_val, card_valb

def find_a_straight(seven):
    #print(seven, 'hello there')
    n = seven
    c = False
    for x in range(0, 8):
        #print(x)
        if ((n[x] == 1 and n[x+1]== 1 and n[x+2] == 1 and n[x+3]==1 and n[x+4]) or (n[0] == 1 and n[9] == 1 and n[10] == 1 and n[11]==1 and n[12] == 1 and n[8]==1)) == 1:
            c = True
            print('yippee!')
            return c
        # else:
        #     c = False
        #     return c

def find_a_flush(suits):
    heart = 0
    club = 0
    spade = 0
    diamond = 0
    for suit in suits:
        if suit == '\u2665':
            heart += 1
            #cs = '\033[1;35;20m blue'
        elif suit == '\u2666':
            #cs =
            diamond += 1
        elif suit =='\u2663':
            #cs = '
            club += 1
        elif suit == '\u2660':
            spade += 1
    print(heart, diamond, spade, club)
    return heart, diamond, spade, club







four_of_a_kind = 0
three_of_a_kind = 0
two_pair = 0
single_pair = 0
full_house = 0
str_aight = 0
flush = 0
straightflush = 0
rotations = 7000
percent_str_flush = 0

for x in range(rotations):
    poss_str_flush_flush = 'b'
    poss_str_flush_str = 'b'
    hand = []
    numbers = []
    suits = []
    while len(hand)< 5:

        card_num = card_name(random.randrange(0, 13))
        card_suit = suit_up(random.randrange(0,4))
        card = card_num + card_suit
        if card not in hand:
            hand.append(card)
            numbers.append(card_num)
            suits.append(card_suit)





    print(hand)
    #print(numbers)
    print(suits)
    seven = check_for_pairsplus(numbers)
    heart, diamond, spade, club  = find_a_flush(suits)
    if (heart == 5 or diamond == 5 or spade == 5 or club == 5):
        if heart == 5:
            suitname = 'hearts'
        elif diamond == 5:
            suitname = 'diamonds'
        elif club == 5:
            suitname = 'clubs'
        elif spade == 5:
            suitname = 'spades'
        print('flush of {}'.format(suitname))
        flush += 1
        poss_str_flush_flush = 'a'


    numpairs = 0
    for b in seven:
        if b == 2:
            numpairs += 1


    print(seven)
    #print(len(seven))
    pair = 0
    if 4 in seven:
        cval = the_num_of_multiples(seven, 4)
        print("\033[1;34;20m Four", cval+'s') #blue
        print("\033[1;37;20m")
        four_of_a_kind += 1
        #quit()
    elif 3 in seven:
        if 2 in seven:
            cval = the_num_of_multiples(seven, 3)
            cval2= the_num_of_multiples(seven, 2)
            print("\033[1;35;20m full house,", cval + 's', 'over ', cval2 + 's') #red
            print("\033[1;37;20m")
            full_house += 1
        else:
            cval = the_num_of_multiples(seven, 3)
            print("\033[1;32;20m three of a kind", cval + 's') #yellow
            print("\033[1;37;20m")
            three_of_a_kind += 1
            percent_threeofakind = three_of_a_kind/rotations

    elif numpairs == 2:
        cval, cval2 = where_are_the_pairs(seven)
        print("\033[1;33;20m 2 pair", cval + 's and ', cval2 + 's') #yellow
        print("\033[1;37;20m")
        percent_two_pair = two_pair / rotations
        two_pair +=1

    elif numpairs == 1:
        cval = the_num_of_multiples(seven, 2)
        print("\033[1;31;20m single pair", cval + 's')  # red
        print("\033[1;37;20m")
        single_pair += 1

    # if 2 in seven:
    #     continue
    # if 3 in seven:
    #     continue
    # if 4 in seven:
    #     continue
    else:
        straight = find_a_straight(seven)
        if straight == True:
            print("\033[1;31;20m straight")  # red
            print("\033[1;37;20m")
            str_aight += 1
            percent_straight = str_aight / rotations
            poss_str_flush_str = 'a'

    if (poss_str_flush_flush == 'a' and poss_str_flush_str == 'a'):
        straightflush += 1
        str_aight -= 1
        percent_str_flush = straightflush /rotations
        print('straightflush')
        poss_str_flush_flush = 'b'
        poss_str_flush_str = 'b'

print("\033[1;34;20mFour of a kinds {}".format(four_of_a_kind))
print("\033[1;32;20mthree of a kinds {} with a percent of {:0.00%}".format(three_of_a_kind, percent_threeofakind))
print("\033[1;33;20m2 pair {} with a percent of {:.0%}".format(two_pair, percent_two_pair))
print("\033[1;31;20mSingle pairs {}".format(single_pair))
print("\033[1;35;20mFullHouse {}".format(full_house))
print("\033[1;36;20mStraight {} with a percent of {}".format(str_aight, percent_straight))
print("\033[1;37;20mFlush {}".format(flush))
print("\033[1;34;20mStraightFlush {} {}".format(straightflush, percent_str_flush))