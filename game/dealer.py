"""
File: dealer.py
Author: Jerry Lane
Purpose: To handle the game action
"""
from game.deck import Deck

# class declaration
class Dealer:
    """
    Parameters: none
    The dealer will shuffle a new Deck, flip over the first one,
    and begin play by asking player if the next is higher or lower.
    If the player guesses correctly, as determined by the Score class,
    the player will add 100 points to their balance. If they guess 
    incorrectly, the player will deduct 75 points from their balance.
    If the balance reaches zero, the game ends.
    """
    def __init__(self):
        self.is_playing = True
        deck = Deck()
        self.previous_card = deck.get_card()
        self.current_card = 0

    def start_game(self):
        while self.is_playing:
            print(f"Previous card: {self.previous_card}")
            choice = input("Will the next card be higher or lower? ")