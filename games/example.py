from components.deck import *
from components.hand import *

def example():
  deck = Deck()
  deck.shuffle()
  trash = Deck(empty=True)
  hand = Hand()

  while True:
    deck.printTop(end=" ")
    trash.printTop(revealed=True)
    print()
    hand.print()
    print()

    i = input("N - nosta kortti\nP - poista kortti\nS - sekoita kortit\nL - Lopeta\n> ").upper()
    if i == "L":
      return
    if i == "N":
      hand.addCard(deck.takeCard())
    if i == "P":
      p = input("Valitse poistettava kortti [1-" + str(len(hand.cards)) + "]\n> ")
      trash.addCard(hand.takeCard(int(p) - 1))
    if i == "S":
      deck.addCards(trash.takeCards(len(trash.cards)))
      deck.shuffle()
