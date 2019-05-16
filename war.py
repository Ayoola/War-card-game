from random import shuffle

# Two useful variables for creating Cards.
suites = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    cards=[]
    for rank in ranks:
        for suite in suites:
            card = (rank,suite)
            cards.append(card)

    def __init__(self,cards=cards):
        self.cards=cards
        return

    def shuffle_deck(self):
        shuffle(self.cards)
        return

    def split_deck(self):
        deck1=self.cards[0:26]
        deck2=self.cards[26:52]
        self.cards=[deck1,deck2]
        return

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards=cards
        return

    def remove_card(self):
        self.cards.pop(0)
        return

    def add_card(self,card):
        self.cards.append(card)
        return


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
card_deck=Deck()
card_deck.shuffle_deck()
card_deck.split_deck()
print(card_deck.cards)
