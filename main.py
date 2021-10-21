# Python 3 program for Elo Rating
import math


class player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = int(rating)

# Function to calculate the Probability
def Probability(rating1, rating2):
  
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))
  
  
# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B. 
def EloRating(player1, player2, K):
   
  
    # To calculate the Winning
    # Probability of Player B
    P2 = Probability(player1.rating, player2.rating)
    P1 = 1 - P2

    player1.rating += (K * (1 - P1))
    player2.rating += (K * (0 - P2))
      
    print("Updated Ratings:-")
    print(player1.name, ": ",  round(player1.rating, 6), player2.name, ": ",  round(player2.rating, 6))
    

    
def main():  
    Will = player("Will", "1200")
    Louie = player("Louie", "1000")
    k = 30
    EloRating(Louie, Will, k)


if __name__ == "__main__":
    main()

# This code is contributed by
# Louie Bond
