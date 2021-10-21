# Python 3 program for Elo Rating
import math, json

Max_Elo_Gain = 50

class player:
    _id = 1
    
    def __init__(self, name):
        self.name = name
        self.elo = 1000
        self.wins = 0
        self.losses = 0
        self.id = player._id
        player._id += 1
        
    def wins(self):
        return (self.wins + self.losses)
    
    def beat(self, other):
        #do the stuff to win a game here
        
        #calc probabilities of both players winning
        P2 = Probability(self.elo, other.elo)
        P1 = 1 - P2
        
        #calc elo gain/loss
        elo_gain = (Max_Elo_Gain * (1 - P1))
        elo_loss = (Max_Elo_gain * (0 - P2))
        
        #update values
        self.elo = elo_gain
        other.elo = elo_loss
        self.wins += 1
        other.losses += 1
        
    def export(self):
        return json.dumps(self.__dict__)

# Function to calculate the Probability
def Probability(elo1, elo2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))
  

if __name__ == "__main__":
    print("Stop running this file!!!")

# This code is contributed by
# Louie Bond
