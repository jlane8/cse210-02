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
        Parameters: self
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
        """
        Parameters: self
        Return: nothing
        The show card method shows the appropriate card, depending on the game phase
        """
        # if in beginning phase, show the card
        if self.phase == 0:        
            print(f"\nThe card is: {str(self.old_card[0])+self.old_card[1]}")
        
        # if second phase, show next card
        elif self.phase == 1:
            print(f"Next card was: {str(self.next_card[0])+self.next_card[1]}")
    
    # method to get the next card from the Deck
    def get_card(self):
        """
        Parameters: self
        Return: nothing
        This method just gets the next card from the Deck and stores it in self.next_card
        """
        # get the next card from the deck and store it in the self.next_card variable
        self.next_card = self.deck.get_card()

    # method to update cards
    def do_updates(self):
        """
        Parameters: self
        Return: nothing
        The do_updates method makes the next card the old card, then gets the next
        card from the Deck
        """
        # store the next_card data in self.old_card, then get a new card for next card
        self.old_card = self.next_card
        self.get_card()
        
    # method to calculate the scores
    def calc_score(self):
        """
        Parameters: self
        Return: nothing
        The calc_score method calculates the players new score. If they guessed correctly,
        the score goes up by 100, if not, it decreases by 75. If the score drops below
        0, the score reflects zero
        """
        # do this while in the beginning phase
        if self.phase == 0:

            # if the player has chosen correctly, add 100 points
            if (self.old_card[0] > self.next_card[0] and self.choice == "l")\
            or (self.old_card[0] < self.next_card[0] and self.choice == "h"):
                self.total_score += 100
            
            # if the player chose incorrectly, deduct 75 points from the score
            else:
                self.total_score -= 75
                if self.total_score < 0:
                    self.total_score = 0
        
    # method to check to see if game should end
    def check_end(self):
        """
        Parameters: self
        Return: nothing
        This method checks to see if the game should end, either because the player selected
        'n' when asked if they wanted to play, or because the score dropped to zero.
        """
        # do this while in the second phase of the game
        if self.phase == 1:

            # if the player has input 'n' in response to the play again prompt or score is zero, 
            # turn off the main game loop and print the final score
            if self.choice == "n" or self.total_score == 0:
                self.is_playing = False
                print(f"\nFinal score: {self.total_score}\nGoodbye!\n")

    # method to output information to the terminal screen
    def do_outputs(self):
        """
        Parameters: self
        Return: nothing
        This method handles screen output, including the prompts for the inputs.
        """
        # show the current card
        self.show_card()

        # get player inputs
        self.get_inputs()

        # calculate the player's score
        self.calc_score()

        # set phase to second half
        self.phase = 1

        # show the next card
        self.show_card()

        # print the player's score
        print(f"Your score is: {self.total_score}")
        
        # ask player if they want to play again, unless the score is zero
        if self.total_score > 0:
            self.get_inputs()

        # check to see if the game should end
        self.check_end()

    # method to get the game inputs
    def get_inputs(self):
        """
        Parameters: self
        Return: nothing
        This method gets the inputs from the user, the prompts reflect the phase of the game.
        """
        # set loop control value to reflect validity of an input
        is_valid = False

        # let loop run until a valid response is given
        while not is_valid:
            
        # temp code to test without being asked if I want to continue

            # get input from player
            choice = input(self.choices[self.phase])
            
            # if in the first phase, and input isn't an 'h' or an 'l', print error message and loop
            if self.phase == 0 and choice != "h" and choice != "l":
                print("Please enter either an 'h' for higher or a 'l' for lower.")

            # if in the first phase and the choice is either an 'h' or an 'l', store the choice
            # and turn off the validity loop by setting the control value to True    
            elif self.phase == 0 and (choice == "h" or choice == "l"):
                self.choice = choice
                is_valid = True

            # if in the second game phase and the input is neither a 'y' or an 'n', print the
            # error message and loop
            elif self.phase == 1 and choice != "y" and choice != "n":
                print("Please enter either a 'y' for yes or an 'n' for no.")

            # if in the second game phase and the input is either a 'y' or an 'n', store the 
            # player's choice and turn off the validity loop    
            elif self.phase == 1 and (choice == "y" or choice == "n"):
                self.choice = choice
                is_valid = True
        
    # method to run the game
    def start_game(self):
        """
        Parameters: self
        Return: nothing
        The start_game method handles the initial running of the game. It also contains the game 
        loop which will run until the score falls to zero or the player chooses to quit.
        """
        # loop to run until player quits or loses all points, all explained above
        while self.is_playing:
            self.do_outputs()
            self.do_updates()
            self.phase = 0