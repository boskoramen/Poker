# Import statements
import references

class Card:
    
    suit = None
    value = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        

    def __str__(self):
        return references.valuesNum[self.value] + ' of ' + references.suitsNum[self.suit]  
   

    def getSuit(self):
        return self.suit

    
    def getValue(self):
        return self.value
