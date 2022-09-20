"""
File: score.py
Author: Jerry Lane
Purpose: This class will hold the score of a player, adjust the 
score based on correct or incorrect bool values, and return the
current score on request.
"""

# score class declaration
class Score:
    """
    Parameters: none
    Return: nothing
    This class represents the score and score manipulations of a
    given player.
    """
    
    # constructor
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        This constructor of the Score class holds a player score, and
        in this initial instanciation, grants the player a beginning 
        balance.
        """
        self.score = 300

    # method to score the choice and amend the object's score
    def choice(self, is_correct):
        """
        Parameters: is_correct - bool representing whether the player guessed
        correctly or not
        Return: current score - after the score has been adjusted according to
        the player's choice.
        """
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

    # method to return current score value
    def get_score(self):
        """
        Parameters: none
        Return: current score
        This method will return the current score of an object
        """
        # return current score
        return self.score