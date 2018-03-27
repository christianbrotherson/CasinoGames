import random
import time

class Player:
  def __init__(self, name, wallet=0, card_count=0):
    self.name = name
    self.wallet = wallet
    self.card_count = card_count

  def update_wallet(self, wallet):
    self.wallet = self.wallet + wallet

  def update_card_count(self, card_number):
    self.card_count = self.card_count + card_number
    card_number = card_number

def deal_card():
  deck = []
  suit = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
  for i in suit.items():
    deck.append(i[1])
  random.shuffle(deck)
  dealt_card = deck.pop()
  return dealt_card

def place_bet(w):
  bet = int(input("How much would you like to bet:"))
  while bet > w:
    if bet > w:
      bet = int(input(f"You do not have enough funds, you have ${w} and bet ${bet}, please enter another bet: "))
    else:
      print(f"You have bet ${bet}.")
  print(f"You have bet ${bet}.")
  return bet

def game_begin(w, p, d):
  print(f"You have ${w}!")
  time.sleep(1)
  bet = place_bet(w)
  time.sleep(1)
  p.update_card_count(deal_card())
  time.sleep(1)
  d.update_card_count(deal_card())
  print(f"Your total card count is {p.card_count}. My total card count is {d.card_count}")
  return bet
 
def deal_another(p, d):
  p.update_card_count(deal_card())
  time.sleep(1)
  if d.card_count < 16:
    d.update_card_count(deal_card())
  time.sleep(1)
  print(f"Your total card count is {p.card_count}")
  
def lost_bet(bet, p):
  return p.update_wallet(-bet)
  
def won_bet(bet, p):
  return p.update_wallet(bet * 1.5)
  
def win_or_lose(p, d, bet):
  if p.card_count > 21:
    print("Dealer Wins")
    return lost_bet(bet, p)
  elif p.card_count < d.card_count:
    if d.card_count <=21:
      print("Dealer Wins!")
      return lost_bet(bet, p)
    else:
      print("You win!")
      return won_bet(bet, p)
  elif p.card_count > d.card_count:
    print("You win!")
    return won_bet(bet, p)

def main():
  name = input("What is your name?").strip()
  wallet = int(input("How much money would you like to add to your wallet?"))
  player_one = Player(name)
  player_one.update_wallet(wallet)
  dealer = Player('dealer')
  another_card = 'yes'
  play_again = 'yes'
  print("Let's play BlackJack!")
  while play_again == 'yes':
    player_one.update_card_count(0)
    dealer.update_card_count(0)
    bet = game_begin(wallet, player_one, dealer)
    while another_card == 'yes':
      deal_another(player_one, dealer)
      another_card = input('Would you like another card?').lower()
    print(win_or_lose(player_one, dealer, bet))
    print(player_one.card_count, dealer.card_count, player_one.wallet)
    player_one.update_wallet(player_one.wallet)
    play_again = input("Would you like to play again?(Yes or No)")
  
  
main()








