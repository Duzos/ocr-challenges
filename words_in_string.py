from util import *

FILE_PATH = "json/words_in_string.txt" # Its not a .json file its a .txt but tough luck 
split = Splitter(FILE_PATH)

def getListOfWords():
    split.rewrite()

    file = open(FILE_PATH, "r")
    lines = file.read()

    return lines.split(" ")

def getAmountOfWords():
    return len(getListOfWords())

compute_line(spin_amount=2,sleep_time=0.5) # Unnecessary but fun
print("There are " + str(getAmountOfWords()) + " words in the file.")
input("Press enter to close..")
    