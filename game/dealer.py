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
        self.score = 0

    # method to collect the input from the player and do minimal validation checking
    def get_input(self, prompt, key):
        """
        Parameters: none
        Return: valid choice or "invalid" to signify a bad input
        This method collects user input, checks to see if input is valid, and returns
        the appropriate information. 
        """
        # get user input
        choice = input(prompt)
        
        # if input h or l and key is 1, return choice
        if (choice == "h" or choice == "l") and key == 1:
            return choice
        
        # if input y or n and key is 2, return choice
        elif (choice == "y" or choice == "n") and key == 2:
            return choice

        # if input is bad, display reason, return "invalid"
        else:
            if key == 1:
                print("Your selection must be an h for higher, or an l for lower.")
            elif key == 2:
                print("Your selection must be a 'y' for yes, or a 'n' for no.")
            if key == 2 and choice == "":
                return "y"
            return "invalid"

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
            print(f"\nThe card is: {self.previous_card}")
            is_valid = False
            high_low = False
            yes_no = False
            
            # loop until valid input is given
            while not is_valid:
                
                # ask user for yes or no, make sure
                if high_low == False and yes_no == False:
                    choice = self.get_input("Higher or lower? [h/l] ", 1)
                
                # if the input is good, run the rest of the program, otherwise loop back for another
                # attempt to validate a good input
                if choice != "invalid" and high_low == False:

                    # show first question's answer is good
                    high_low = True

                    # get the next card from the Deck
                    self.current_card = self.deck.get_card()

                    # print the current card so user can see what it is
                    print(f"Next card was: {self.current_card}")

                    # handle the user's higher choice:
                    # if h is True, send to calc_score
                    # otherwise send False to calc_score
                    if choice == "h" and self.current_card > self.previous_card:
                        self.score = self.calc_score(True)
                    elif choice == "h" and self.current_card <= self.previous_card:
                        self.score = self.calc_score(False)

                    # handle lower choice
                    # if l is True, send to calc_score
                    # otherwise send False to calc_score
                    if choice == "l" and self.current_card < self.previous_card:
                        self.score = self.calc_score(True)
                    elif choice == "l" and self.current_card >= self.previous_card:
                        self.score = self.calc_score(False)

                # ask user if they want to play again
                if high_low == True and yes_no == False:
                    play = self.get_input("Play again? [y/n] ", 2)

                    # check for valid answer and run appropriately
                    if play != "invalid" and high_low == True and yes_no == False:

                        # show answer was either a y or n
                        yes_no = True
                        
                        # end turn control loop
                        is_valid = True

                        # move current card to previous card in preparation of next loop, if applicable
                        self.previous_card = self.current_card

                        # handle quit choice or balance dropping to zero, end game
                        if play == "n" or self.score == 0:
                            self.is_playing = False
                        
                        # display score in case of continuing, quitting, or game ending 
                        if self.is_playing:
                            print(f"Current score: {self.score}")
                        else:
                            print(f"Final score: {self.score}\n")

    def calc_score(self, is_correct):
         
         # if player guessed correctly, add 100 to the score
        if is_correct:
            self.score += 100

        # if not, subtract 75 from the current score    
        elif not is_correct:
            self.score -= 75

        # if balance drops below 0, balance = 0
        if self.score < 0:
            self.score = 0
        
        # return new current score
        return self.score