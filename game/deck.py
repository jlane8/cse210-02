"""
File: deck.py
Author: Jerry Lane
Purpose: Handles the cards in the deck created by Dealer
"""
import random

# class declaration
class Deck:
    deck = []

    def __init__(self):
        self.card = 1
        self.shuffle()

    def shuffle(self):
        
        # zero deck out
        #self.deck = []

        # put four sets of 13 cards in the deck
        for index in range(0, 4):
            for index2 in range(1, 14):
                self.deck.append(index2)
        
        self.show_deck()
        print("Finished with setup.")

    def get_card(self):
        limit = len(self.deck) - 1
        print(f"Deck size: {limit + 1}")
        select = random.randint(0, limit)
        print(f"Selected: {select}")
        value = self.deck[select]
        print(f"Value: {value}")
        del self.deck[select]
        return value

    def show_deck(self):
        for i in range(len(self.deck)):
            print(f"Card: {self.deck[i]}")