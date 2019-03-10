class Options:
    def check(amount):
        return amount

    def call(amount,bet):
        return amount + bet

    def raise(amount, raiseAmount):
        return amount + raiseAmount

    def fold(amount):
        return amount

class GamePlay:
    from deck import Deck
    buttonPosition=0
    amount = 0
    players = []
    Amount = []
    stakes = 50;

    def handlesBlinds(pos,numPlayers):
            self.buttonPosition+=1
            if pos == numPlayers-1:
                self.buttonPosition=0
            smallBlind = self.stakes/2
            bigBlind = self.stakes
            smallBlindPosition = self.buttonPosition+1
            bigBlindPosition = self.buttonPosition+2
            if pos == smallBlindPosition:
                return smallBlind
            elif pos == bigBlindPosition:
                return bigBlind
            else
                return 0

    def preflop(self):
            for i in range(len(self.players)):
                    Amount[i] = handlesBlinds(i,len(self.players))



            for pos in self.players:
                decision = decision() #AI program to be implemented later, output is either call,check,raise, or bet
                if decision == "call"





