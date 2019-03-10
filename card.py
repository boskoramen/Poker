# Import statements
import references

class Card:
    
    suit = None
    value = None
    hidden = None
    
    def __init__(self, suit, value, hidden=False):
        self.suit = suit
        self.value = value
        self.hidden = hidden
        

    def __str__(self):
        return references.valuesNum[self.value] + ' of ' + references.suitsNum[self.suit]  
   

    def getSuit(self):
        return self.suit

    
    def getValue(self):
        return self.value

    def isHidden(self):
        return self.hidden
