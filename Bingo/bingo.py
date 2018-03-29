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
from bingo_card import BingoCardNumbers
from bingo_display import BingoDisplay
from next_number import NextNumber

def main():
  player_card_numbers = BingoCardNumbers()
  player_card_display = BingoDisplay()
  card_nums = player_card_numbers.get_random_numbers_for_card()
  win = GraphWin('BINGO', 600, 800, autoflush=False)
  win.setBackground(color_rgb(191, 191, 191))
  b,i,n,g,o = player_card_numbers.assign_rand_nums_to_bingo(card_nums)
  background_change = player_card_display.display_player_card(b,i,n,g,o,win)
  player_card_display.in_circle(background_change, win)
  win.getMouse()

  
main()