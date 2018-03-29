import random
from graphics import *
import math

class BingoCardNumbers:

  def __init__(self):
    self.b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    self.i_list = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    self.n_list = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    self.g_list = [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    self.o_list = [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]

  def get_random_numbers_for_card(self):
    bingo = self.b_list, self.i_list, self.n_list, self.g_list, self.o_list
    card_numbers_list = []
    for y, single_list in enumerate(bingo):
      x = 0
      if bingo[y] != self.n_list:
        while x < 5:
          rand_num = random.choice(bingo[y])
          bingo[y].remove(rand_num)
          card_numbers_list.append(rand_num)
          x += 1
      else:
        while x < 4:
          rand_num = random.choice(bingo[y])
          bingo[y].remove(rand_num)
          card_numbers_list.append(rand_num)
          x += 1
    player_card_numbers = card_numbers_list[::-1]
    return player_card_numbers

  def assign_rand_nums_to_bingo(self, player_card_numbers):
    b, i, n, g, o = [],[],[],[],[]
    bingo = b,i,n,g,o
    for a, num_lists in enumerate(bingo):
      y = 0
      if len(player_card_numbers) > 14:
        while y < 5:
          bingo[a].append(player_card_numbers.pop())
          y += 1
      elif 11 < len(player_card_numbers) < 15:
        while y < 4:
          bingo[a].append(player_card_numbers.pop())
          y += 1
      else:
        while y < 5:
          bingo[a].append(player_card_numbers.pop())
          y += 1
    return b,i,n,g,o