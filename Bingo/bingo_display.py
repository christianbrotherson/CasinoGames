import math
from graphics import *

class BingoDisplay():

  def __init__(self):
    self.background_change = []

  def display_player_card(self, b, i, n, g, o, win):
  # BINGO Header
      B = Text(Point(108, 58), "B")
      B.setSize(36)
      B.setStyle('bold')
      B.draw(win)
      I = Text(Point(204, 58), "I")
      I.setSize(36)
      I.setStyle('bold')
      I.draw(win)
      N = Text(Point(300, 58), "N")
      N.setSize(36)
      N.setStyle('bold')
      N.draw(win)
      G = Text(Point(396, 58), "G")
      G.setSize(36)
      G.setStyle('bold')
      G.draw(win)
      O = Text(Point(492, 58), "O")
      O.setSize(36)
      O.setStyle('bold')
      O.draw(win)

  # Card Boxes
      border = Rectangle(Point(50,100), Point(550,600))
      border.setFill('black')
      border.draw(win)
      r1c1 = Circle(Point(108, 158), 48)
      r1c1.setFill('white')
      r1c1.draw(win)
      r1c2 = Circle(Point(204, 158), 48)
      r1c2.setFill('white')
      r1c2.draw(win)
      r1c3 = Circle(Point(300, 158), 48)
      r1c3.setFill('white')
      r1c3.draw(win)
      r1c4 = Circle(Point(396, 158), 48)
      r1c4.setFill('white')
      r1c4.draw(win)
      r1c5 = Circle(Point(492, 158), 48)
      r1c5.setFill('white')
      r1c5.draw(win)
      r2c1 = Circle(Point(108, 254), 48)
      r2c1.setFill('white')
      r2c1.draw(win)
      r2c2 = Circle(Point(204, 254), 48)
      r2c2.setFill('white')
      r2c2.draw(win)
      r2c3 = Circle(Point(300, 254), 48)
      r2c3.setFill('white')
      r2c3.draw(win)
      r2c4 = Circle(Point(396, 254), 48)
      r2c4.setFill('white')
      r2c4.draw(win)
      r2c5 = Circle(Point(492, 254), 48)
      r2c5.setFill('white')
      r2c5.draw(win)
      r3c1 = Circle(Point(108, 350), 48)
      r3c1.setFill('white')
      r3c1.draw(win)
      r3c2 = Circle(Point(204, 350), 48)
      r3c2.setFill('white')
      r3c2.draw(win)
      r3c3 = Circle(Point(300, 350), 48)
      r3c3.setFill('white')
      r3c3.draw(win)
      r3c4 = Circle(Point(396, 350), 48)
      r3c4.setFill('white')
      r3c4.draw(win)
      r3c5 = Circle(Point(492, 350), 48)
      r3c5.setFill('white')
      r3c5.draw(win)
      r4c1 = Circle(Point(108, 446), 48)
      r4c1.setFill('white')
      r4c1.draw(win)
      r4c2 = Circle(Point(204, 446), 48)
      r4c2.setFill('white')
      r4c2.draw(win)
      r4c3 = Circle(Point(300, 446), 48)
      r4c3.setFill('white')
      r4c3.draw(win)
      r4c4 = Circle(Point(396, 446), 48)
      r4c4.setFill('white')
      r4c4.draw(win)
      r4c5 = Circle(Point(492, 446), 48)
      r4c5.setFill('white')
      r4c5.draw(win)
      r5c1 = Circle(Point(108, 542), 48)
      r5c1.setFill('white')
      r5c1.draw(win)
      r5c2 = Circle(Point(204, 542), 48)
      r5c2.setFill('white')
      r5c2.draw(win)
      r5c3 = Circle(Point(300, 542), 48)
      r5c3.setFill('white')
      r5c3.draw(win)
      r5c4 = Circle(Point(396, 542), 48)
      r5c4.setFill('white')
      r5c4.draw(win)
      r5c5 = Circle(Point(492, 542), 48)
      r5c5.setFill('white')
      r5c5.draw(win)
      self.background_change = [r1c1,r2c1,r3c1,r4c1,r5c1,r1c2,r2c2,r3c2,r4c2,r5c2,r1c3,r2c3,r3c3,r4c3,r5c3,r1c4,r2c4,r3c4,r4c4,r5c4,r1c5,r2c5,r3c5,r4c5,r5c5]
 
  # Free Space
      free_space = Text(Point(300,350), "Free Space")
      free_space.setSize(15)
      free_space_background = r3c3
      free_space_background.setFill('lightBlue')
      free_space.draw(win)
  
  # Number assignment to win
      def display_b_nums(b):
        y = 158
        for i in b:
          B = Text(Point(108, y), i)
          B.setSize(18)
          B.draw(win)
          y += 96
      def display_i_nums(i):
        y = 158
        for x in i:
          I = Text(Point(204, y), x)
          I.setSize(18)
          I.draw(win)
          y += 96
      def display_n_nums(n):
        B = Text(Point(300, 158), n[0])
        B.setSize(18)
        B.draw(win)
        I = Text(Point(300, 254), n[1])
        I.setSize(18)
        I.draw(win)
        G = Text(Point(300, 446), n[2])
        G.setSize(18)
        G.draw(win)
        O = Text(Point(300, 542), n[3])
        O.setSize(18)
        O.draw(win)
      def display_g_nums(g):
        y = 158
        for i in g:
          G = Text(Point(396, y), i)
          G.setSize(18)
          G.draw(win)
          y += 96
      def display_o_nums(o):
        y = 158
        for i in o:
          O = Text(Point(492, y), i)
          O.setSize(18)
          O.draw(win)
          y += 96
      display_b_nums(b)
      display_i_nums(i)
      display_n_nums(n)
      display_g_nums(g)
      display_o_nums(o)

      ready = Text(Point(300, 700), 'Click anywhere to begin!')
      ready.setSize(36)
      ready.setStyle('bold')
      ready.draw(win)
      win.getMouse()
      ready.undraw()

      return self.background_change


    # Determines which circle is being selected.
  def in_circle(self, background_change, win):
    match = Text(Point(300, 650), 'Click on the numbers that match!')
    match.setSize(20)
    match.draw(win)
    click = win.getMouse()
    for i, circ in enumerate(background_change):
      dx = click.getX() - circ.getCenter().getX()
      dy = click.getY() - circ.getCenter().getY()
      dist = math.sqrt(dx*dx + dy*dy)
      if dist <= circ.getRadius():
        circ.setFill('lightBlue')

    
    # def update_card(self, win):