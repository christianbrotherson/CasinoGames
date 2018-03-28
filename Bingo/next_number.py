import random

class NextNumber():

  def __init__(self):
    self.bingo_num_list = []
    self.selected_nums = []
    self.num = 0

  def generate_list(self):
    for i in range(76):
      self.bingo_num_list.append(i)
    return self.bingo_num_list

  def new_num(self):
    # TODO: build in a catch to make sure the same number is not selected more than once.
    bingo_num_list = self.generate_list()
    self.num = random.choice(bingo_num_list)
    self.selected_nums.append(self.num)
    return self.num, self.selected_nums