import random
from graphics import *

class BingoCard:

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

  def display_player_card(self, b, i, n, g, o, win):
    border = Rectangle(Point(10,110), Point(490,590)).draw(win)
    vert_line_one = Line(Point(106, 110), Point(106, 590)).draw(win)
    vert_line_two = Line(Point(202, 110), Point(202, 590)).draw(win)
    vert_line_three = Line(Point(298, 110), Point(298, 590)).draw(win)
    vert_line_four = Line(Point(394, 110), Point(394, 590)).draw(win)
    horiz_line_one = Line(Point(10, 206), Point(490, 206)).draw(win)
    horiz_line_two = Line(Point(10, 302), Point(490, 302)).draw(win)
    horiz_line_three = Line(Point(10, 398), Point(490, 398)).draw(win)
    horiz_line_four = Line(Point(10, 494), Point(490, 494)).draw(win)
    B = Text(Point(58, 58), "B")
    B.setSize(36)
    B.setStyle('bold')
    B.draw(win)
    I = Text(Point(154, 58), "I")
    I.setSize(36)
    I.setStyle('bold')
    I.draw(win)
    N = Text(Point(250, 58), "N")
    N.setSize(36)
    N.setStyle('bold')
    N.draw(win)
    free_space = Text(Point(250,355), "Free Space")
    free_space.setSize(15)
    free_space.draw(win)
    G = Text(Point(346, 58), "G")
    G.setSize(36)
    G.setStyle('bold')
    G.draw(win)
    O = Text(Point(442, 58), "O")
    O.setSize(36)
    O.setStyle('bold')
    O.draw(win)
    def display_b_nums(b):
      y = 159
      for i in b:
        B = Text(Point(58, y), i)
        B.setSize(18)
        B.draw(win)
        y += 98

    def display_i_nums(i):
      y = 159
      for x in i:
        I = Text(Point(154, y), x)
        I.setSize(18)
        I.draw(win)
        y += 98

    def display_n_nums(n):
      B = Text(Point(250, 159), n[0])
      B.setSize(18)
      B.draw(win)
      I = Text(Point(250, 257), n[1])
      I.setSize(18)
      I.draw(win)
      G = Text(Point(250, 453), n[2])
      G.setSize(18)
      G.draw(win)
      O = Text(Point(250, 551), n[3])
      O.setSize(18)
      O.draw(win)
        

    def display_g_nums(g):
      y = 159
      for i in g:
        G = Text(Point(346, y), i)
        G.setSize(18)
        G.draw(win)
        y += 98

    def display_o_nums(o):
      y = 159
      for i in o:
        O = Text(Point(442, y), i)
        O.setSize(18)
        O.draw(win)
        y += 98

    display_b_nums(b)
    display_i_nums(i)
    display_n_nums(n)
    display_g_nums(g)
    display_o_nums(o)
