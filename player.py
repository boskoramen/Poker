# Import statements
from deck import Deck

class Player:

    # The name of the player
    name = None

    # The player's current hand
    hand = None

    # The amount of money the player is better in the current hand
    bet = None

    # Roles are dealer, big blind, and small blind
    role = None

    # The amount of money that the player has
    balance = None

    def __init__(self,
                 name='Default Name',
                 hand = [],
                 bet = 0,
                 role = None,
                 balance = 0
    ):
        self.name = name
        self.hand = hand
        self.bet = bet
        self.role = role
        self.balance = balance


    def addToHand(self, card):
        """ 
        Adds a Card object to the player's hand
        """
        self.hand.append(card)


    def increaseBet(self, bet):
        """ 
        Increases the amount of money the player is betting for the current hand
        """
        self.bet += bet

        
    def setRole(self, role):
        """ 
        Sets the role of the player for the current hand
        """
        self.role = role


    def increaseBalance(self, num):
        """
        Increases the player's balance by num
        """
        self.balance += num


    def decreaseBalance(self, num):
        """
        Decreases the player's balance by num
        """
        self.balance -= num

        
    def getName(self):
        """ 
        Returns the name of the player
        """
        return self.name


    def getHand(self):
        """ 
        Returns the name of the player
        """
        return self.hand


    def getBet(self):
        """ 
        Returns the name of the player
        """
        return self.bet


    def getRole(self):
        """ 
        Returns the role of the player
        """
        return self.role
