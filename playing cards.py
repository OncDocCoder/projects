import random

class Card(object):
    def __init__(self, suit, val):
        self.suit =  suit
        self.value = val

    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = 'A'
        elif self.value == 11:
            val = 'J'
        elif self.value == 12:
            val = 'Q'
        elif self.value ==13:
            val = 'K'
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        for card in self.cards:
            print(card.show())

    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def shuffle(self, num = 1):
        random.shuffle(self.cards)

    def deal(self, n_players, n_cards):
        self.hands = [self.cards[i:n_players* n_cards:n_players] for i in range(0, n_players)]

myDeck = Deck()
myDeck.shuffle()

myDeck.deal(3,5)
print(*myDeck.hands, sep= '\n')

