# Import statements
import random

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

                
    def shuffle(self):
        random.shuffle(cards)


    def draw(self):
        return cards.pop()
