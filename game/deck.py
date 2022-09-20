"""
File: deck.py
Author: Jerry Lane
Purpose: Handles the cards in the deck created by Dealer
"""
import random

# class declaration
class Deck:
    
    
    # global deck, so all methods can access it
    deck = []

    # constructor
    def __init__(self):
        self.card = 1
        self.shuffle()

    # set up, renew deck
    def shuffle(self):
        
        # zero deck out
        self.deck = []

        # put four sets of 13 cards in the deck
        for m in range(0, 4):
            for index2 in range(1, 14):
                self.deck.append(index2)

    # randomly select new card, renew deck when halfway
    def get_card(self):
        limit = len(self.deck) - 1
        select = random.randint(0, limit)
        value = self.deck[select]
        del self.deck[select]
        if len(self.deck) < 26:
            self.shuffle()
        return value