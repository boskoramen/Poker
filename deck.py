# Import statements
from card import Card
import references

class Deck:
    
    cards = None

    def __init__(self):
        self.cards = []

        for suit in references.suits:
            for value in references.values:
                card = Card(references.suits[suit], references.values[value])
                self.cards.append(card)

                
    def test(self):
        for card in self.cards:
            print(str(card))
