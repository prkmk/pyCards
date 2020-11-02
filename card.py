import enum
from colorama import init, Fore, Back, Style
from cardCharacters import *

class Suits(enum.Enum):
  HEART = "♥"
  SPADE = "♠"
  DIAMOND = "♦"
  CLUB = "♣"

class Card:
  def __init__(self, suit = Suits.HEART, value = 1, revealed = True):
    self.value = 14 if value == 1 else value
    self.suit = suit
    self.revealed = revealed
    if suit == Suits.HEART:
      self.character = HEARTS[value - 2]
    if suit == Suits.SPADE:
      self.character = SPADES[value - 2]
    if suit == Suits.DIAMOND:
      self.character = DIAMONDS[value - 2]
    if suit == Suits.CLUB:
      self.character = CLUBS[value - 2]
  
  def print(self, end = "\n"):
    try:
      if self.revealed:
        f = Fore.RED if (self.suit == Suits.HEART or self.suit == Suits.DIAMOND) else Fore.BLACK
        print(f + Back.WHITE + self.character + " " + Style.RESET_ALL, end=end)
      else:
        print(Fore.BLACK + Back.WHITE + BACK + " " + Style.RESET_ALL, end=end)
    except:
      if self.revealed:
        print(self.character + " ", end=end)
      else:
        print(BACK + " ", end=end)
    
  def reveal(self):
    self.revealed = True
  
  def hide(self):
    self.revealed = False
  
  def flip(self):
    self.revealed = not self.revealed