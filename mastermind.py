import random
import json

JSON_PATH = "json/mastermind.json"

def splitNumberIntoDigitList(digits: int):
    return [int(d) for d in str(digits)]
   
def countValidNumbers(generated: int, player: int):
    gList = splitNumberIntoDigitList(generated)
    pList = splitNumberIntoDigitList(player)
    valid = 0
   
    for i in gList:
        if i in pList:
            del pList[valid-1]
            valid = valid + 1
   
    return valid
   
def getValidNumberPositions(generated: int, player: int):
    valid = []
    gList = splitNumberIntoDigitList(generated)
    pList = splitNumberIntoDigitList(player)
       
    count = 0
    for i in gList:
        count = count + 1
        if i == pList[count-1]:
            valid.append(count)
           
   
    return valid
   
def getIntSize(input: int):
    return len(splitNumberIntoDigitList(input))
   
def isIntRightSize(input: int, size: int):
    return getIntSize(input) == size
     
def getPlayerInput(target: int):
    player = int(input("Input number "))
    size = getIntSize(target)
   
    if (isIntRightSize(player,size) == False):
        print("Invalid int length, must be " + str(size) + " digits.")
        player = getPlayerInput(target)
       
    return player
     
def isEasy():
    print("Do you want to play on easy mode y/n")
    b = input().lower()
   
    if (b == "y"):
        return True
    elif (b == "n"):
        return False
    else:
        print("Invalid input, defaulting to hard mode.")
        return False
     
def getTable():
    with open(JSON_PATH,'r') as f:
        table = json.load(f)
    return table

def getScoreForPlayer(player: str):
    with open(JSON_PATH,'r') as f:
        table = json.load(f)
    return table[player]

def getHighScore():
    with open(JSON_PATH,'r') as f:
        table = json.load(f)
    highest = 0
    for score in table.values():
        if score < highest:
            highest = score
    return highest

def getHighScorePlayer():
    with open(JSON_PATH,'r') as f:
        table = json.load(f)
    highest = 0
    high_player = ""
    for player in table.keys():
        if player[0] > highest:
            highest = player[0]
            high_player = player
    return player

def writeScore(player: str, score: int):
    with open(JSON_PATH,'r') as f:
        table = json.load(f)
    print(table)
    print(score)
    table[player] = score
    with open(JSON_PATH,'w') as w:
        json.dump(table, w, indent=4)
    

def guessLoop(target: int, easy: bool):
    player = getPlayerInput(target)

    if(player == target):
        return True
       
    valid = countValidNumbers(target,player)
    print(str(valid) +" matching number(s)")
   
    if (easy and valid > 0):
        pos = getValidNumberPositions(target,player)
        msg = "There are valid numbers in positions:"
       
        if (len(pos) == 0):
            return False
       
        for i in pos:
            msg = msg + " " + str(i)
           
        print(msg)
       
    return False
     
def main():
    easy = isEasy()
    generated = random.randint(0,9999)

    if (easy == False):
        generated = random.randint(0,99999)
   
    tries = 0
    success = False
    while success == False:
        tries = tries + 1
        success = guessLoop(generated, easy)
       
    print("Congratulations, you won after " + str(tries) + " tries!")
    name = input("What is your username?\n")
    print("Writing score..")

    writeScore(name,tries)

    print("Score written!")
    print("High score: " + str(getHighScore()))
    input()
   
main()