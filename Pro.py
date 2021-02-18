import random

###     PART 1      ###
###     Setting up the deck of cards and assigning values to all card types     ###

### Build the card classes ###

suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


###     PART 2      ###
###     HOW CARDS WILL BE VIEWED AS WELL AS THEIR RANKS     ###
class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getValue(self):
        return values[self.rank]

    def __str__(self):
        rankstr = self.rank
        suitstr = self.suit
        if self.rank == 'J':
            rankstr = 'Jack'
        elif self.rank == 'Q':
            rankstr = 'Queen'
        elif self.rank == 'K':
            rankstr = 'King'
        elif self.rank == 'A':
            rankstr = 'Ace'
        if self.suit == 'S':
            suitstr = 'Spades'
        elif self.suit == 'H':
            suitstr = 'Hearts'
        elif self.suit == 'C':
            suitstr = 'Clubs'
        elif self.suit == 'D':
            suitstr = 'Diamonds'
        return "{x} of {y}".format(x=rankstr, y=suitstr)


###     PART 3      ###
###     HOW HANDS ARE MADE AND HOW THE DECK IS SHUFFLED AND DEALT     ###

class Hand():

    def __init__(self, playername):
        self.myCards = []
        self.playername = playername

    def __str__(self):
        for card in self.myCards:
            print(card)
        return ''

    def __len__(self):
        return len(self.myCards)

    def add_card(self, card):
        self.myCards.append(card)


class Deck():

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def __str__(self):
        for card in self.cards:
            print(card)
        return ''

    def __len__(self):
        return len(self.cards)

    def deal_card(self):
        return self.cards.pop()


###     PART 4      ###
###     HOW THE GAME IS PLAYED WITH ROUND WINNERS DECIDED BY CARD VALUE     ###

def playcards(hand1, hand2, warcards=[]):
    card1 = hand1.myCards.pop() ## ALIAS from myCards array
    card2 = hand2.myCards.pop() ## ALIAS from myCards array

    print("{a}: {b}".format(a=player1name, b=card1))
    print("{c}: {d}".format(c=player2name, d=card2))

    print()

    if card1.getValue() == card2.getValue():
        print('This means WAR')
        print()
        war(hand1, hand2, card1, card2)
    elif card1.getValue() > card2.getValue():
        print("{a} wins!".format(a=player1name))
        hand1.myCards.insert(0, card1)
        hand1.myCards.insert(0, card2)
        for card in warcards:
            hand1.myCards.insert(0, card)
    else:
        print("{b} wins!".format(b=player2name))
        hand2.myCards.insert(0, card1)
        hand2.myCards.insert(0, card2)
        for card in warcards:
            hand2.myCards.insert(0, card)


###     PART 5      ###
###     HOW THE GAME HANDLES WAR WITH PLAYERS PLACING THREE CARDS DOWN      ###

def war(hand1, hand2, card1, card2):
    warcards1 = [card1]
    warcards2 = [card2]
    i = 3
    while i > 0:
        warcards1.append(hand1.myCards.pop())
        warcards2.append(hand2.myCards.pop())
        i = i - 1
    print("Player 1 Cards:")
    for card in warcards1:
        print(card) ## card is referring to different elements of warcards1 - REFRENCE
    print()
    print("Player 2 Cards:")
    for card in warcards2: ## card is referring to different elements of warcards2 - REFERENCE
        print(card)
    print()
    playcards(hand1, hand2, warcards1 + warcards2)


###     PART 6      ###
###     HOW THE GAME WILL START; USERS INPUTTING THEIR NAMES AND GAME RULES     ###

maindeck = Deck()

print()
print("The Rules of War: ")
print()
print("Two players are engaged in war!")
print()
print("The deck is split between the two and each plays a card;")
print("the highest card wins the round and collects both cards.")
print("If there is a tie, that means war!")
print("Both players place three cards in the pot,")
print("then each play their next card.")
print("War will continue as long as there is a tie.")
print("The game will be played until a player runs out of cards.")
print("The player with cards remaining is the victor!")
print()
print("The game could go on for a large amount of time, so be prepared!")
print()

###     PLAYERS NAMING THEMSELVES WITH USER INPUT      ###
player1name = input('Player 1 Name: ')
if player1name == '':
    player1name = 'Player 1: '
hand1 = Hand(player1name)
hand_x = Hand(player1name) ## shallow copy of hand1


player2name = input('Player 2 Name: ')
if player2name == '':
    player2name = 'Player 2'
hand2 = Hand(player2name)
hand_y = Hand(player2name) ## hand_y shallow copy of hand2

###     HOW THE GAME IS BEING PLAYED BY THE PLAYERS     ###
while len(maindeck) > 0:
    hand1.add_card(maindeck.deal_card())
    hand2.add_card(maindeck.deal_card())

while len(hand1) > 0 and len(hand2) > 0:
    print("Next Round: ")
    print(player1name + " has " + str(len(hand1.myCards)) + " cards")
    print(player2name + " has " + str(len(hand2.myCards)) + " cards")
    print()
    playcards(hand1, hand2)

    print()

    keepPlaying = input('Press any key to continue or press E to Exit.').upper()
    if keepPlaying == 'E':
        break
    print()

print(hand1)
print(len(hand1))
print(hand2)
print(len(hand2))
print(hand2.myCards.pop())
