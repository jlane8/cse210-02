"""
file: __main__.py
Author: Jerry Lane
Purpose: Entry point for Hilo game.
"""
# import dealer class
from game.dealer import Dealer

# create dealer object, use dealer's start_game method to start game
dealer = Dealer()
dealer.start_game()