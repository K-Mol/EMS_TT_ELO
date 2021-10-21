# Python 3 program for Elo Rating
import math

Max_Elo_Gain = 50

class player:
    _id = 1
    
    def __init__(self, name):
        self.name = name
        self.elo = 1000
        self.wins = 0
        self.losses = 0
        self.id = player._id
        player._id
        
    def wins(self):
        return (self.wins + self.losses)
    
   def gamewon(self, other):
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

# Function to calculate the Probability
def Probability(elo1, elo2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))
  
  
# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B. 
def EloRating(winner, loser, K):
   
  
    # To calculate the Winning
    # Probability of Player B
    P2 = Probability(winner.rating, loser.rating)
    P1 = 1 - P2

    winner.rating += (K * (1 - P1))
    loser.rating += (K * (0 - P2))
      
    print("Updated Ratings:-")
    print(winner.name, ": ",  round(winner.rating, 6), loser.name, ": ",  round(loser.rating, 6))
    

    
def main():  
    Will = player("Will", "1200")
    Louie = player("Louie", "1000")
    k = 30
    EloRating(Louie, Will, k)


if __name__ == "__main__":
    main()

# This code is contributed by
# Louie Bond, Sam Allix

