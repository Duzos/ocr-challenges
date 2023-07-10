from util import *

FILE_PATH = "json/letter_list.txt" # Its not a .json file its a .txt but tough luck 
split = Splitter(FILE_PATH)

def getListOfWords():
    split.rewrite()

    file = open(FILE_PATH, "r")
    lines = file.read()

    return lines.split(" ")

def getListStartingWithChar(char: str):
    if (len(char) > 1):
        print("Character length longer than 1")
        return []
    
    list = []

    for word in getListOfWords():
        if (word[0] == char):
            list.append(word)

    return list

def getAmountOfListStartingWithChar(char: str):
    return len(getListStartingWithChar(char))

def printWordList(list: list):
    list.sort()
    for word in list:
        print(word)

def main():
    char = input("Letter: ").lower()
    compute_line(spin_amount=2,sleep_time=0.5) # Unnecessary but fun
    list = getListStartingWithChar(char)
    print("\n")
    printWordList(list)
    print("There are " + str(len(list)) + " words starting with " + char)

    input("Press enter to close..")
    
if __name__ == "__main__":
    main()