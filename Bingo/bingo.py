# Create the bingo card Class
  # 5x5 with bingo signifying the columns.
    # B - ranges from 1-15
    # I - ranges from 15-30
    # N - ranges from 31-45 with the blank space in the middle
    # G - ranges from 46-60
    # O - ranges from 61-75
  # Need a random selector method that will randomly select 5 different numbers (4 in N) for each letter.
  # Need a graphics window that will display the card with their numbers.
  # Need a update method that will update the graphics window after every number that is drawn.

# Need to incorporate the Player class from the blackjack game and make sure that I can create players and update their losses and winnings.

from graphics import *
import random

from bingo_card import BingoCard
from next_number import NextNumber

def main():
  player_card = BingoCard()
  player_card_numbers = player_card.get_random_numbers_for_card()
  win = GraphWin('BINGO', 500, 800)
  b,i,n,g,o = player_card.assign_rand_nums_to_bingo(player_card_numbers)
  player_card.display_player_card(b,i,n,g,o,win)
  win.getMouse()
  
main()  