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
        self.is_playing = True
        self.deck = Deck()
        self.previous_card = self.deck.get_card()
        self.current_card = 0
        self.score_object = Score()
        self.score = self.score_object.get_score()

    # method to collect the input from the player and do minimal validation checking
    def get_input(self):
        """
        Parameters: none
        Return: valid choice or "invalid" to signify a bad input
        This method collects user input, checks to see if input is valid, and returns
        the appropriate information. 
        """
        # get user input
        choice = input("Will the next card be (h)igher or (l)ower (or (q)uit)? ")
        
        # if input doesn't consist of h, l, or q, display error message to user and return "invalid"
        if choice != "h" and choice != "l" and choice != "q":
            print("Your selection must be a q for quit, an h for higher, or an l for lower.")
            return "invalid"
        
        # if input is good, return valid choice
        else:
            return choice

    # method which controls game play
    def start_game(self):
        """
        Parameters: none
        Return: nothing
        This method controls the game play. While the bool variable is_pplaying is true, the 
        loop will print out the previous card, call the get_input method, and if the input
        is valid, it will get a new card. The score object method is called to score the user's
        choice. If the score reaches 0, the game ends, otherwise it will loop until the user quits.
        """
        # main game loop starts by printing out the previous card and setting the validate loop control
        while self.is_playing:
            print(f"\nPrevious card: {self.previous_card}")
            is_valid = False
            
            # loop until valid input is given
            while not is_valid:
                choice = self.get_input()
                
                # if the input is good, run the rest of the program, otherwise loop back for another
                # attempt to validate a good input
                if choice != "invalid":

                    # get the next card from the Deck
                    self.current_card = self.deck.get_card()

                    # print the current card so user can see what it is
                    print(f"Current card: {self.current_card}")
                    
                    # since the input was valid, turn off the validate input loop
                    is_valid = True

                    # handle the user's higher choice:
                    # notify Score object's method of correct or incorrect choice
                    # and let Score method adjust the score accordingly
                    if choice == "h" and self.current_card > self.previous_card:
                        self.score = self.score_object.choice(True)
                        print("Correct! ", end="")
                    elif choice == "h" and self.current_card <= self.previous_card:
                        self.score = self.score_object.choice(False)
                        print("Sorry, incorrect! ", end="")

                    # handle lower choice
                    # notify Score object's method of correct or incorrect choice
                    # and let Score method adjust the score accordingly
                    if choice == "l" and self.current_card < self.previous_card:
                        self.score = self.score_object.choice(True)
                        print("Correct! ", end="")
                    elif choice == "l" and self.current_card >= self.previous_card:
                        self.score = self.score_object.choice(False)
                        print("Sorry, incorrect! ", end="")
                    
                    # handle quit choice or balance dropping to zero
                    if choice == "q" or self.score == 0:
                        self.is_playing = False
                    
                    # display score in case of continuing, quitting, or game ending 
                    if self.is_playing:
                        print(f"Current score: {self.score}")
                    else:
                        print(f"Final score: {self.score}\n")
                    
                    # move current card to previous card in preparation of next loop
                    self.previous_card = self.current_card