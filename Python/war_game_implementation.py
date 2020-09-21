#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITE = 'H D S C'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.first_hand = None
        self.second_hand = None
        self.deck = []
        for num in SUITE:
            for alpha in RANKS:
                self.deck.append(alpha+num)
    def half_cut(self):
        shuffle(self.deck)
        self.first_hand = self.deck[:26]
        self.second_hand = self.deck[26:]
        return (self.first_hand, self.second_hand)




class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, deck):
        self.hand = deck

    def add(self, card):
        self.hand.extend(card)

    def remove(self):
        if len(self.hand)>0:
            return self.hand.pop(0)

        else:
            print('Empty hand!')

    def __str__(self):
        return "Contains {} cards".format(len(self.hand))

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play(self):
        card = self.hand.remove()
        print('{} has remove {}'.format(self.name, card))
        return card
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.hand)<3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.hand.pop())
            return war_cards


    def still_has_cards(self):
        return len(self.hand.hand)!=0

######################
#### GAME PLAY #######
######################
# print("Welcome to War, let's begin...")
print("Welcome to War, let's begin...")

# Create New Deck and split in half
d = Deck()
half1,half2 = d.half_cut()

# Create Both Players
comp = Player("computer",Hand(half1))
name = input("What is your name player? ")
user = Player(name,Hand(half2))

# Set Round Count
total_rounds = 0
war_count = 0
# Let's play
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" count: "+str(len(user.hand.hand)))
    print(comp.name+" count: "+str(len(comp.hand.hand)))
    print("Both players play a card!")
    print('\n')

    # Cards on Table represented by list
    table_cards = []

    # Play cards
    c_card = comp.play()
    p_card = user.play()
    # Add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        # Check to see who had higher rank
        if RANKS.index(c_card[:-1]) < RANKS.index(p_card[:-1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[:-1]) < RANKS.index(p_card[:-1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
