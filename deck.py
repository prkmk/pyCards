from card import *
import random

class Deck:
  def __init__(self, empty = False):
    self.cards = []
    if not empty:
      for suit in Suits:
        for value in range(2, 15):
          self.cards.append(Card(suit, value))

  def print(self):
    for card in self.cards:
      card.print()

  def printTop(self, revealed = False, end = "\n"):
    if len(self.cards) > 0:
      if not revealed:
        Card(revealed=False).print(end=end)
      else:
        self.cards[len(self.cards) - 1].print(end=end)
    else:
      print("   ", end=end)

  def shuffle(self):
    random.shuffle(self.cards)
  
  def takeCard(self):
    if len(self.cards) > 0:
      return self.cards.pop()
    else:
      return None
  
  def takeCards(self, count = 1):
    count = len(self.cards) if count > len(self.cards) else count
    cards = []
    for i in range(count):
      cards.append(self.cards.pop())
    return cards
  
  def addCard(self, card):
    if card != None:
      self.cards.append(card)
    return len(self.cards)
  
  def addCards(self, cards):
    for card in cards:
      self.cards.append(card)
    return len(self.cards)