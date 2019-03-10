from card import Card

suits = {
    'HEARTS':0,
    'DIAMONDS':1,
    'SPADES':2,
    'CLUBS':3,
}

values = {
    'ACE':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'JACK':11,
    'QUEEN':12,
    'KING':13
}

class Deck:
       
    cards = None

    def __init__(self):
        cards = []
        
        for suit in suits:
            for value in values:
                cards.append(Card(suit, value))

    def test(self):
        print(self.cards)
