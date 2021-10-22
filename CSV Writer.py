import csv

def RobustIntInput(Text):
    while True:
        try:
            Input = int(input(Text))
        except:
            continue
        break
    
    return Input

def CalculatingRatingChange(Player1Elo,Player2Elo,Results,KVal = 25):
    #Results are from player one's perspectve 
    Player1Elo = int(Player1Elo)
    Player2Elo = int(Player2Elo)

    Player1ExpectedScore = len(Results)/(1 + (8**((Player2Elo-Player1Elo)/400)))

    Player1RatingChange = KVal*(sum(Results) - Player1ExpectedScore)

    Player2ExpectedScore =  len(Results)/(1 + (8**((Player1Elo-Player2Elo)/400)))

    Player2RatingChange = KVal*(sum([1-Val for Val in Results]) - Player2ExpectedScore)

    return (round(Player1Elo + Player1RatingChange),round(Player2Elo + Player2RatingChange))

def CheckingIfWorks():
    import random
    ListOfPlayers = [(1000,random.randint(1,100)) for _ in range(10)]

    print(ListOfPlayers)

    for _ in range(3):
        for a in range(len(ListOfPlayers)):
            for b in range(len(ListOfPlayers)):
                if a == b:continue

                NewVals = CalculatingRatingChange(ListOfPlayers[a][0],ListOfPlayers[b][0],[int(ListOfPlayers[a][1]>ListOfPlayers[b][1])])
                ListOfPlayers[a] = (round(NewVals[0]),ListOfPlayers[a][1])
                ListOfPlayers[b] = (round(NewVals[1]),ListOfPlayers[b][1])


    print(sorted(ListOfPlayers,key = (lambda x : x[0])))
    print("")
    print(sorted(ListOfPlayers,key = (lambda x : x[1])))

def ChangingCSV():

    file = open('Players.csv')

    csvreader = csv.reader(file)
    Rows = []
    for row in csvreader:
        Rows.append(row)
    file.close()

    print(Rows[0])
    for i in range(1,len(Rows)):
        print("["+str(i)+"] " + Rows[i][0] + " : " + Rows[i][1])
    
    Player1Index = RobustIntInput("What is the number of player 1? ")

    while Player1Index not in range(1,len(Rows)):
        print("That doesn't work")
        Player1Index = RobustIntInput("What is the number of player 1 ?")

    Player2Index = int(input("What is the number of player 2? "))

    while Player2Index not in range(1,len(Rows)):
        print("That doesn't work")
        Player1Index = RobustIntInput("What is the number of player 2 ?")

    Player1 = Rows[Player1Index]
    Player2 = Rows[Player2Index]

    NumberOfGames = int(input("How many Games were played? "))

    Player1Wins = int(input("How many did "+ Player1[0]+" win? "))

    Results = [1 for _ in range(Player1Wins)] + [0 for _ in range(NumberOfGames - Player1Wins)]

    print(Results)

    NewElo = CalculatingRatingChange(Player1[1],Player2[1],Results)

    print(NewElo)

    Rows[Player1Index][1] = NewElo[0]
    Rows[Player2Index][1] = NewElo[1]

    f = open('Players.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)

    for Row in Rows:
        writer.writerow(Row)
    
    f.close()

def ClearingCSV():

    file = open('Players.csv')

    csvreader = csv.reader(file)
    Rows = []
    for row in csvreader:
        Rows.append(row)
    file.close()

    f = open('Players.csv', 'w')

    writer = csv.writer(f)

    for Row in Rows:
        if Row[0] == "Andrew Hanneman":
            writer.writerow([Row[0], 1002])
            continue
        writer.writerow([Row[0], 1000])
        
    
    f.close()


print(CalculatingRatingChange(1000,1000,[1]))
ChangingCSV()
