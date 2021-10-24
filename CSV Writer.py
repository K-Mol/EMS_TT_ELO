import csv

def RobustIntInput(Text):
    while True:
        try:
            Input = int(input(Text))
        except:
            continue
        break
    
    return Input

def CalculatingRatingChange(Player1Elo,Player2Elo,NumberOfGames,Player1Wins,KVal = 25):
    #Results are from player one's perspectve 
    Player1Elo = int(Player1Elo)
    Player2Elo = int(Player2Elo)

    Player1ExpectedScore = NumberOfGames/(1 + (8**((Player2Elo-Player1Elo)/400)))

    Player1RatingChange = KVal*(Player1Wins - Player1ExpectedScore)

    Player2ExpectedScore =  NumberOfGames/(1 + (8**((Player1Elo-Player2Elo)/400)))

    Player2RatingChange = KVal*((NumberOfGames-Player1Wins) - Player2ExpectedScore)

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
        Player1Index = RobustIntInput("What is the number of player 1? ")

    Player2Index = int(input("What is the number of player 2?"))

    while ((Player2Index not in range(1,len(Rows))) or (Player2Index == Player1Index)):
        print("That doesn't work")
        Player2Index = RobustIntInput("What is the number of player 2? ")

    Player1 = Rows[Player1Index]
    Player2 = Rows[Player2Index]

    NumberOfGames = int(input("How many Games were played? "))

    Player1Wins = int(input("How many did "+ Player1[0]+" win? "))

    NewElo = CalculatingRatingChange(Player1[1],Player2[1],NumberOfGames,Player1Wins)

    #Headers = ["Player Name", "Elo", "Total Wins", "Total Losses", " Total Games Played", "Win Percentage"]

    Player1NewRow = [Player1[0],NewElo[0], int(Player1[2])+Player1Wins, int(Player1[3])+NumberOfGames-Player1Wins, int(Player1[4]) + NumberOfGames, round(100* ((int(Player1[2])+Player1Wins)/(int(Player1[4]) + NumberOfGames)))]

    Player2NewRow = [Player2[0],NewElo[0], int(Player2[2])+NumberOfGames-Player1Wins, int(Player2[3])+Player1Wins, int(Player2[4]) + NumberOfGames, round(100* ((int(Player2[2])+NumberOfGames-Player1Wins)/(int(Player2[4]) + NumberOfGames)))]
    
    Rows[Player1Index] = Player1NewRow
    Rows[Player2Index] = Player2NewRow 

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
            writer.writerow([Row[0], 1002] + [0 for _ in range(len(Rows[0])-2)])
            continue
        writer.writerow([Row[0], 1000] + [0 for _ in range(len(Rows[0])-2)])
        
    f.close()

def DisplayingStats():
    file = open('Players.csv')

    csvreader = csv.reader(file)
    Rows = []
    for row in csvreader:
        Rows.append(row)
    file.close()
    
    print("/n".join(Rows))

def AddingAPlayer(PlayerName, StartingRating = 1000 ,Headers = ["Player Name ", "Elo ", "Total Wins ", "Total Losses ", "Total Games Played ", "Win Percentage "]):
    f = open('Players.csv', 'a')

    writer = csv.writer(f)
    writer.writerow([PlayerName, StartingRating] + [0 for _ in range(len(Headers)-2)])

def InitialisingCSV(Headers = ["Player Name ", "Elo ", "Total Wins ", "Total Losses ", "Total Games Played ", "Win Percentage "]):
    f = open('Players.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(Headers)
    f.close()
    
print(CalculatingRatingChange(1000,1000,1,1))
InitialisingCSV()
AddingAPlayer("Kyle Molindo",StartingRating = 1000)
AddingAPlayer("Freddie Hancock",StartingRating = 1000)
ChangingCSV()
DisplayingStats()
