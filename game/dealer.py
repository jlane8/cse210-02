"""
File: dealer.py
Author: Jerry Lane
Purpose: To handle the game action
"""
# import the Deck class for the cards in Hilo
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
     
    # initial constructor method 
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This constructor will turn on the game play loop (is_playing),
        create new Deck and Score objects, get the first previous card
        using a Deck method, set current card to 0 (this will be updated
        when the current card is drawn in the game loop), and collect the
        current score from the Score method and store it in the self.score
        variable.
        """
        # main game control variable - set to play
        self.is_playing = True

        # instantiate the Deck and set default values for cards
        self.deck = Deck()
        self.old_card = self.deck.get_card()
        self.next_card = self.deck.get_card()
        
        # set initial player score
        self.total_score = 300
        
        # set the phase the game is in for input and card display
        self.phase = 0

        # set choices
        self.choices = ["Higher or lower? [h/l] ", "Play again? [y/n] "]

    # method to display appropriate card
    def show_card(self):
        if self.phase == 0:        
            print(f"\nThe card is: {str(self.old_card[0])+self.old_card[1]}")
        elif self.phase == 1:
            print(f"Next card was: {str(self.next_card[0])+self.next_card[1]}")
    
    # method to get the next card from the Deck
    def get_card(self):
        self.next_card = self.deck.get_card()

    # method to update cards
    def do_updates(self):
        self.old_card = self.next_card
        self.get_card()
        
    # method to calculate the scores
    def calc_score(self):
        if self.phase == 0:
            if (self.old_card[0] > self.next_card[0] and self.choice == "l")\
            or (self.old_card[0] < self.next_card[0] and self.choice == "h"):
                self.total_score += 100
            else:
                self.total_score -= 75
                if self.total_score < 0:
                    self.total_score = 0
        
    # method to check to see if game should end
    def check_end(self):
        if self.phase == 1:
            if self.choice == "n" or self.total_score == 0:
                self.is_playing = False
                print(f"\nFinal score: {self.total_score}\nGoodbye!\n")

    # method to output information to the terminal screen
    def do_outputs(self):
        self.show_card()
        self.get_inputs()
        self.calc_score()
        self.phase = 1
        self.show_card()
        print(f"Your score is: {self.total_score}")
        if self.total_score > 0:
            self.get_inputs()
        self.check_end()

    # method to get the game inputs
    def get_inputs(self):
        is_valid = False
        # set loop to run until a valid response is given
        while not is_valid:
            choice = input(self.choices[self.phase])
            if self.phase == 0 and choice != "h" and choice != "l":
                print("Please enter either an 'h' for higher or a 'l' for lower.")
            elif self.phase == 0 and (choice == "h" or choice == "l"):
                self.choice = choice
                is_valid = True
            elif self.phase == 1 and choice != "y" and choice != "n":
                print("Please enter either a 'y' for yes or an 'n' for no.")
            elif self.phase == 1 and (choice == "y" or choice == "n"):
                self.choice = choice
                is_valid = True
        
    # method to run the game
    def start_game(self):

        # loop to run until player quits or loses all points
        while self.is_playing:
            self.do_outputs()
            self.do_updates()
            self.phase = 0