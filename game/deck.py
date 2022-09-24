"""
File: deck.py
Author: Jerry Lane
Purpose: Handles the cards in the Deck
"""
# import the random module to use it in randomly selecting a new card from the deck
import random

# class declaration
class Deck:
    """
    This class represents a common card deck of four suits with thirteen
    cards in each suit. It has methods in it to handle shuffling (setting up
    the deck for initial use), and a second to get a new card from the deck.
    The variables it tracks are the current deck makeup, and current card.
    """    
    
    # global deck, (and suits list) so all methods can access it
    deck = []
    suits = [] # not yet implemented - for future development

    # constructor
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This is the constructor method, setting an Ace up as initial card, and 
        causing the deck to be populated with the equivalent of four suits of 
        thirteen cards in each suit.
        """
        self.card = 1
        self.shuffle()

    # set up, renew deck
    def shuffle(self):
        """
        Parameters: none
        Return: nothing
        This method populates the deck with 52 cards. The list represents four
        suits of thirteen cards each.
        """
        
        # zero deck out so the completed deck has exactly 52 cards
        self.deck = []

        # put four sets of 13 cards in the deck, one for each suit
        for suit in range(0, 4):
            for value in range(1, 14):
                self.deck.append(value)
                self.suits.append(suit)

    # randomly select new card, renew deck when halfway
    def get_card(self):
        """
        Parameters: none
        Return: value of the card drawn
        This method will randomly draw a card from the deck, delete the card from the deck,
        and return it to the dealer for use. if the deck is over half used, it will call the
        shuffle method to renew the deck.
        """
        # set the top limit of the random selection to one below the length of the deck list
        # this keeps the random selection within index range
        limit = len(self.deck) - 1

        # select the next card from the deck randomly
        select = random.randint(0, limit)

        # get the value of the card and store it in a variable
        if self.suits[select] == 0:
            suit = "\033[1;30m\u2660\033[00m"
        elif self.suits[select] == 1:
            suit = "\033[1;30m\u2663\033[00m"
        elif self.suits[select] == 2:
            suit = "\033[1;31m\u2665\033[00m"
        elif self.suits[select] == 3:
            suit = "\033[1;31m\u2666\033[00m"
        value = [self.deck[select], suit]

        # delete the card from the deck
        del self.deck[select]
        del self.suits[select]

        # if the deck is over half used, shuffle a new one up
        if len(self.deck) < 26:
            self.shuffle()
        
        # return the value of the newly drawn card
        return value