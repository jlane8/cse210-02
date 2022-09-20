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
        self.score = 300

    # method to score the choice and amend the object's score
    def choice(self, is_correct):
        if is_correct:
            self.score += 100
        elif not is_correct:
            self.score -= 75
        if self.score <= 0:
            self.score = 0
        return self.score

    # method to return current score value
    def get_score(self):
        return self.score