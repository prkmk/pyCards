from components.deck import *
from components.hand import *

def solitaire():
  deck = Deck()
  deck.shuffle()
  trash = Deck(empty=True)
  numOfTrash = 3
  tableDecks = []
  tableDeckCount = 7
  for i in range(tableDeckCount):
    tableDecks.append(Deck(empty=True))
  buildDecks = []
  for suit in Suits:
    buildDecks.append(Deck(empty=True))
  
  def shuffleTable():
    for i in range(len(tableDecks)):
      for j in range(i):
        tableDecks[i].addCard(deck.takeCard())
      tableDecks[i].addCard(deck.takeCard().reveal())

  def printTable():
    deck.printTop(end=" ")
    print("   ", end=" ")

    for i in range(len(tableDecks)):
      diff = len(tableDecks) - len(buildDecks) # 3
      if i - diff >= 0:
        buildDecks[i - diff].printTop(end=" ")
      else:
        print("   ", end=" ")
    
    print()
    print()

    maxDeckLength = 0
    for d in tableDecks:
      maxDeckLength = len(d.cards) if len(d.cards) > maxDeckLength else maxDeckLength

    for i in range(maxDeckLength):
      if i < numOfTrash and trash.hasCards():
        trash.printCard(len(trash.cards) - numOfTrash + i, end=" ")
      elif i == 0:
        trash.printCard(0, end=" ")
      else: 
        print("   ", end=" ")
      print("   ", end=" ")

      for j in range(len(tableDecks)):
        if tableDecks[j].hasCards():
          tableDecks[j].printCard(i, end=" ")
        elif i == 0:
          tableDecks[j].printCard(i, end=" ")
        else:
          print("   ", end=" ")

      print()
  
  def printOptions():
    print("r  - reveal cards from deck")
    print("XX - move card from pile (from to, 0-" + str(tableDeckCount) + ")")
    print("X  - move card up (0-" + str(tableDeckCount) + ")")
    print("q  - quit")

  shuffleTable()

  while True:
    printTable()
    print()
    printOptions()
    i = input("> ").upper()

    if i == "Q": return
    if i == "R":
      if deck.hasCards():
        for i in range(numOfTrash if len(deck.cards) > numOfTrash else len(deck.cards)):
          trash.addCard(deck.takeCard().reveal())
      else:
        deck.addCards(trash.takeAllCards())
        deck.hideAll()
    elif len(i) == 2:
      fr = int(i[0])
      to = int(i[1])
      if fr <= tableDeckCount and 1 <= to <= tableDeckCount:
        if fr == 0:
          tableDecks[to - 1].addCard(trash.takeCard())
        else:
          tableDecks[to - 1].addCard(tableDecks[fr - 1].takeCard())
          tableDecks[fr - 1].revealTop()
    elif len(i) == 1:
      fr = int(i[0])
      if fr <= tableDeckCount:
        card = Card()
        if fr == 0:
          card = trash.takeCard()
        else:
          card = tableDecks[fr - 1].takeCard()
          tableDecks[fr - 1].revealTop()
        if card.suit == Suits.HEART:
          buildDecks[0].addCard(card)
        if card.suit == Suits.SPADE:
          buildDecks[1].addCard(card)
        if card.suit == Suits.DIAMOND:
          buildDecks[2].addCard(card)
        if card.suit == Suits.CLUB:
          buildDecks[3].addCard(card)
    
    print()