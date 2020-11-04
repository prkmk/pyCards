from components.deck import *
from components.hand import *

def solitaire():
  deck = Deck()
  deck.shuffle()
  trash = Deck(empty=True)
  table = [
    Deck(empty=True),
    Deck(empty=True),
    Deck(empty=True),
    Deck(empty=True),
    Deck(empty=True),
    Deck(empty=True),
    Deck(empty=True)
  ]

  def shuffleTable():
    for i in range(len(table)):
      for j in range(i):
        table[i].addCard(deck.takeCard())
      table[i].addCard(deck.takeCard().reveal())

  def printTable():
    maxDeckLength = 0
    for d in table:
      maxDeckLength = len(d.cards) if len(d.cards) > maxDeckLength else maxDeckLength

    for i in range(maxDeckLength):
      for d in table:
        d.printCard(i, end=" ")
      print()
  
  shuffleTable()
  printTable()