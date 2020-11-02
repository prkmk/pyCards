from card import *
import random

def suit(card):
  if card.suit == Suits.HEART:
    return 1
  if card.suit == Suits.SPADE:
    return 2
  if card.suit == Suits.DIAMOND:
    return 3
  if card.suit == Suits.CLUB:
    return 4

def value(card):
  return card.value

def revealed(card):
  return not card.revealed

def sortCards(cards):
  cards.sort(key=suit)
  cards.sort(key=value)
  cards.sort(key=revealed)

class Hand:
  def __init__(self, cards = []):
    self.cards = cards
    sortCards(self.cards)

  def print(self, end = "\n"):
    if len(self.cards) > 0:
      for card in self.cards:
        if card == self.cards[len(self.cards) - 1]:
          card.print(end=end)
        else:
          card.print(end=" ")
    else:
      print(end=end)
  
  def addCard(self, card):
    if card != None:
      self.cards.append(card)
      sortCards(self.cards)
    return len(self.cards)
  
  def addCards(self, cards):
    for card in cards:
      self.cards.append(card)
    sortCards(self.cards)
    return len(self.cards)

  def takeCard(self, index):
    if index < len(self.cards): 
      return self.cards.pop(index)
    else:
      return None

  def revealCard(self, index):
    self.cards[index].reveal()
    sortCards(self.cards)

  def hideCard(self, index):
    self.cards[index].hide()
    sortCards(self.cards)

  def flipCard(self, index):
    self.cards[index].flip()
    sortCards(self.cards)
  
  def hideAll(self):
    for card in self.cards:
      card.hide()
  
  def revealAll(self):
    for card in self.cards:
      card.reveal()
    sortCards(self.cards)