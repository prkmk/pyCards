from components.deck import *
from components.hand import *

def example():
  deck = Deck()
  deck.shuffle()
  trash = Deck(empty=True)
  hand = Hand()

  while True:
    deck.printTop(end=" ")
    trash.printTop()
    print()
    hand.print()
    print()

    if deck.hasCards():
      print("N - nosta kortti")
    if hand.hasCards():
      print("P - poista kortti")
    print("S - sekoita kortit")
    print("L - Lopeta")
    i = input("> ").upper()
    if i == "L":
      return
    if i == "N" and deck.hasCards():
      hand.addCard(deck.takeCard().reveal())
    if i == "P" and hand.hasCards():
      p = input("Valitse poistettava kortti [1-" + str(len(hand.cards)) + "]\n> ")
      try:
        trash.addCard(hand.takeCard(int(p) - 1))
      except:
        trash.addCard(hand.takeCard(0))
    if i == "S":
      deck.addCards(trash.takeCards(len(trash.cards)))
      deck.hideAll()
      deck.shuffle()
