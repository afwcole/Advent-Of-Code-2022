def getStrongerPlayThan(thisPlay):
    potentialPlays = [1, 2, 3]
    return potentialPlays[(thisPlay + 3) % 3]

def getWeakerPlayThan(thisPlay):
    return getStrongerPlayThan(thisPlay - 2)

def calcMySpeculativeRoundScore(elfValue, myValue):
    if myValue == getStrongerPlayThan(elfValue):
        return myValue + 6
    elif myValue == elfValue:
        return myValue + 3
    else:
        return myValue

def calcMyRealRoundScore(elfValue, myValue):
    if myValue == 2: #Draw
        return elfValue + 3
    elif myValue == 3: #Win
        return getStrongerPlayThan(elfValue) + 6
    else: #Lose
        return getWeakerPlayThan(elfValue)


with open('/Users/adriancole/Desktop/Advent-Of-Code-2022/rock_day2/input.txt', 'r') as strategy_file:
    strategy_data = strategy_file.readlines()
    processed_data = [_.strip().split(" ") for _ in strategy_data]
    
    gameValues = {
        'A' : 1, #Rock
        'B' : 2, #Paper
        'C' : 3, #Scissors
        'X' : 1, #(Rock) Lose
        'Y' : 2, #(Paper) Draw
        'Z' : 3  #(Scissors) Win
    }

    mySpeculativeScore, myRealScore = 0, 0
    for round in processed_data:
        elfValue, myValue = gameValues[round[0]], gameValues[round[1]]
        mySpeculativeScore += calcMySpeculativeRoundScore(elfValue, myValue)
        myRealScore += calcMyRealRoundScore(elfValue, myValue)

    print(mySpeculativeScore)
    print(myRealScore)