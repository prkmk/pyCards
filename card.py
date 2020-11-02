import enum
from colorama import init, Fore, Back, Style

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
  
  def print(self, end = "\n"):
    try:
      if self.revealed:
        f = Fore.RED if (self.suit == Suits.HEART or self.suit == Suits.DIAMOND) else Fore.BLACK
        b = Back.WHITE
        v = "J" if self.value == 11 else "Q" if self.value == 12 else "K" if self.value == 13 else "A" if self.value == 14 else self.value
        s = self.suit.value + "{:>2}".format(v)
        print(f + b + s + Style.RESET_ALL, end=end)
      else:
        print(Back.GREEN + "   " + Style.RESET_ALL, end=end)
    except:
      if self.revealed:
        v = "J" if self.value == 11 else "Q" if self.value == 12 else "K" if self.value == 13 else "A" if self.value == 14 else self.value
        print(self.suit.value + "{:>2}".format(v), end=end)
      else:
        print("███", end=end)
        
    
  def reveal(self):
    self.revealed = True
  
  def hide(self):
    self.revealed = False
  
  def flip(self):
    self.revealed = not self.revealed