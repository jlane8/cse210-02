"""
File: dealer.py
Author: Jerry Lane
Purpose: To handle the game action
"""
from game.deck import Deck
from game.score import Score

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
        self.deck = Deck()
        self.previous_card = self.deck.get_card()
        self.current_card = 0
        self.score_object = Score()
        self.score = self.score_object.get_score()

    def get_input(self):
        choice = input("Will the next card be (h)igher or (l)ower (or (q)uit)? ")
        if choice != "h" and choice != "l" and choice != "q":
            print("Your selection must be a q for quit, an h for higher, or an l for lower.")
            return "invalid"
        else:
            return choice

    def start_game(self):
        while self.is_playing:
            print(f"\nPrevious card: {self.previous_card}")
            is_valid = False
            while not is_valid:
                choice = self.get_input()
                if choice != "invalid":
                    self.current_card = self.deck.get_card()
                    print(f"Current card: {self.current_card}")
                    is_valid = True
                    
                    # handle higher choice
                    if choice == "h" and self.current_card > self.previous_card:
                        self.score = self.score_object.choice(True)
                        print("Correct! ", end="")
                    elif choice == "h" and self.current_card <= self.previous_card:
                        self.score = self.score_object.choice(False)
                        print("Sorry, incorrect! ", end="")

                    # handle lower choice
                    if choice == "l" and self.current_card < self.previous_card:
                        self.score = self.score_object.choice(True)
                        print("Correct! ", end="")
                    elif choice == "l" and self.current_card >= self.previous_card:
                        self.score = self.score_object.choice(False)
                        print("Sorry, incorrect! ", end="")
                    
                    # handle quit choice or balance dropping to zero
                    if choice == "q" or self.score == 0:
                        self.is_playing = False
                    
                    # display score    
                    if self.is_playing:
                        print(f"Current score: {self.score}")
                    else:
                        print(f"Final score: {self.score}")
                    
                    # move current card to previous card
                    self.previous_card = self.current_card
