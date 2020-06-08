import math

# x = int(input('the number you want to find factorial of'))
# a = math.factorial(x)
# print(a)

#royal flush
no_fivecardhands= math.factorial(52)/(math.factorial(5)*math.factorial(47))
#odds_r_flush = 1/r_flush
print ('there are  {:,}'.format(no_fivecardhands), 'five-card hands' )
royal_flush = no_fivecardhands/4
print('the chance of getting a royal flush is 1 in {:,.0f}'.format(royal_flush))
straight_flush = no_fivecardhands/36
print('the chance of getting a straight, non-royal flush is 1 in {:,.0f}'.format(straight_flush))
four_ofakind = no_fivecardhands/624
print('the chance of getting a 4 of a kind is 1 in {:,.0f}'.format(four_ofakind))
full_house = no_fivecardhands/3744
print('the chance of getting a fullhouse is 1 in {:,.2f}'.format(full_house))
flush = no_fivecardhands/5108
print('the chance of getting a flush is 1 in {:,.2f}'.format(flush))
straight= no_fivecardhands/10200
print('the chance of getting a straight is 1 in {:,.2f}'.format(straight))
three_of_a_kind = no_fivecardhands/54912
print('the chance of getting three of a kind is 1 in {:,.2f}'.format(three_of_a_kind))
two_pair = no_fivecardhands/123552
print('the chance of getting two pair is 1 in {:,.2f}'.format(two_pair))
one_pair = no_fivecardhands/1098240
print('the chance of getting one pair is 1 in {:,.2f}'.format(one_pair))

# X is the number of a certain card in the deck
# Y is the total number of cards in the deck
# Z is the number of cards drawn
# N is the number you are checking for
# H (n) = C (X, n) * C (Y – X, Z – n) / C (Y, Z)



x = 2
y = 47
z = 3
n = 2
solution = c (X, n) * C (Y – X, Z – n) / C (Y, Z)