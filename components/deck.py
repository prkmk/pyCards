from components.card import *
import random

class Deck:
  def __init__(self, empty = False):
    self.cards = []
    if not empty:
      for suit in Suits:
        for value in range(2, 15):
          self.cards.append(Card(suit, value, False))

  def print(self):
    for card in self.cards:
      card.print()

  def revealTop(self):
    if len(self.cards) > 0:
      self.cards[len(self.cards) - 1].reveal()

  def printTop(self, end = "\n"):
    self.printCard(len(self.cards) - 1, end=end)

  def printCard(self, index, end = "\n"):
    if not self.hasCards():
      try:
        print(Back.LIGHTBLACK_EX + "   " + Style.RESET_ALL, end=end)
      except:
        print("███", end=end)
    if len(self.cards) > index and index >= 0:
      self.cards[index].print(end=end)
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

  def hasCards(self):
    return len(self.cards) > 0

  def hideAll(self):
    for card in self.cards:
      card.hide()
  
  def revealAll(self):
    for card in self.cards:
      card.reveal()